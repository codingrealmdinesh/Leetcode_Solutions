class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * cols for _ in range(rows)]

        def get_min_health(currCell, nextRow, nextCol):
            if nextRow >= rows or nextCol >= cols:
                return float('inf')
            nextCell = dp[nextRow][nextCol]
            # hero needs at least 1 point to survive
            return max(1, nextCell - currCell)

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                currCell = dungeon[row][col]

                right_health = get_min_health(currCell, row, col+1)
                down_health = get_min_health(currCell, row+1, col)
                next_health = min(right_health, down_health)

                if next_health != float('inf'):
                    min_health = next_health
                else:
                    min_health = 1 if currCell >= 0 else (1 - currCell)

                dp[row][col] = min_health

        return dp[0][0]
###
class MyCircularQueue:
    def __init__(self, capacity):
        """
        Set the size of the queue to be k.
        """
        self.queue = [0]*capacity
        self.tailIndex = 0
        self.capacity = capacity

    def enQueue(self, value):
        """
        Insert an element into the circular queue.
        """
        self.queue[self.tailIndex] = value
        self.tailIndex = (self.tailIndex + 1) % self.capacity

    def get(self, index):
        return self.queue[index % self.capacity]


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows, cols = len(dungeon), len(dungeon[0])
        # Use a circular queue to keep a sliding window of DP values
        dp = MyCircularQueue(cols)

        def get_min_health(currCell, nextRow, nextCol):
            if nextRow < 0 or nextCol < 0:
                return float('inf')
            index = cols * nextRow + nextCol
            nextCell = dp.get(index)
            # hero needs at least 1 point to survive
            return max(1, nextCell - currCell)

        for row in range(rows):
            for col in range(cols):
                # iterate the grid in the reversed order
                currCell = dungeon[rows-row-1][cols-col-1]

                right_health = get_min_health(currCell, row, col-1)
                down_health = get_min_health(currCell, row-1, col)
                next_health = min(right_health, down_health)

                if next_health != float('inf'):
                    min_health = next_health
                else:
                    min_health = 1 if currCell >= 0 else (1 - currCell)

                dp.enQueue(min_health)
        # return the last element in the queue
        return dp.get(cols-1)