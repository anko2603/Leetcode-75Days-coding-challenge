# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
# Example 1:
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            
            curr_sum += node.val
            

            paths = prefix_sums.get(curr_sum - targetSum, 0)
            
            
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            
            
            paths += dfs(node.left, curr_sum)
            paths += dfs(node.right, curr_sum)
            

            prefix_sums[curr_sum] -= 1
            
            return paths
        

        prefix_sums = {0: 1}
        return dfs(root, 0)
