class Solution:
    def recoverTree(self, root: TreeNode):
        """
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def inorder(r: TreeNode) -> List[int]:
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        def find_two_swapped(nums: List[int]) -> (int, int):
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    # first swap occurence
                    if x == -1:     
                        x = nums[i]
                    # second swap occurence
                    else:           
                        break
            return x, y
        
        def recover(r: TreeNode, count: int):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return      
                recover(r.left, count)
                recover(r.right, count)
            
        nums = inorder(root)
        x, y = find_two_swapped(nums)
        recover(root, 2)
###
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # predecessor is a Morris predecessor. 
        # In the 'loop' cases it could be equal to the node itself predecessor == root.
        # pred is a 'true' predecessor, 
        # the previous node in the inorder traversal.
        x = y = predecessor = pred = None
        
        while root:
            # If there is a left child
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:       
                # Predecessor node is one step left 
                # and then right till you can.
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
 
                # set link predecessor.right = root
                # and go to explore left subtree
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                # break link predecessor.right = root
                # link is broken : time to change subtree and go right
                else:
                    # check for the swapped nodes
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred 
                    pred = root
                    
                    predecessor.right = None
                    root = root.right
            # If there is no left child
            # then just go right.
            else:
                # check for the swapped nodes
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred 
                pred = root
                
                root = root.right
        
        x.val, y.val = y.val, x.val