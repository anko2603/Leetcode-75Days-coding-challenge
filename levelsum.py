# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
# Example 1:
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0 
        queue = deque([root])
        max_sum = float('-inf')
        min_level = 1
        current_level = 1
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                min_level = current_level
            
            current_level += 1
        
        return min_level
