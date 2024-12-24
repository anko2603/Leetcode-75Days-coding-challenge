# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.
# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            
            is_good = 1 if node.val >= max_val else 0
            

            max_val = max(max_val, node.val)
            
            
            left_good = dfs(node.left, max_val)
            right_good = dfs(node.right, max_val)
            
            return is_good + left_good + right_good
        

        return dfs(root, root.val)
