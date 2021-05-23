class Codec:
    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []
        
    def int_to_str(self, x):
        """
        Encodes integer to bytes string.
        """
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
        
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """
        lst = self.postorder(root)
        lst = [self.int_to_str(x) for x in lst]
        return 'ç'.join(map(str, lst))
    
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
        
    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """
        def helper(lower = float('-inf'), upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root
        
        data = [self.str_to_int(x) for x in data.split('ç') if x]
        return helper() 
###
class Codec:
    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []
        
    def int_to_str(self, x):
        """
        Encodes integer to bytes string
        """
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
        
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """
        lst = [self.int_to_str(x) for x in self.postorder(root)]
        return ''.join(map(str, lst))
    
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
        
    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """
        def helper(lower = float('-inf'), upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root
        
        n = len(data)
        # split data string into chunks of 4 bytes
        # and convert each chunk to int
        data = [self.str_to_int(data[4 * i : 4 * i + 4]) for i in range(n // 4)]
        return helper() 