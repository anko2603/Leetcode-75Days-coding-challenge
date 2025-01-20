# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# Example 1:
# Input: cost = [10,15,20]
# Output: 15
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev1, prev2 = cost[0], cost[1]
        
        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev1, prev2 = prev2, current
        
        return min(prev1, prev2)
