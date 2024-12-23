# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
# Example 1:
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeafValues(root):
            leaf_values = []
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    if not node.left and not node.right:  
                        leaf_values.append(node.val)
                    else:
                        stack.append(node.right)
                        stack.append(node.left)
            return leaf_values
        
        
        leaves1 = getLeafValues(root1)
        leaves2 = getLeafValues(root2)
        

        return leaves1 == leaves2
