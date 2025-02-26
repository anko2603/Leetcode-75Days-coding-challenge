# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:
# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
# For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
# In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
# If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
# A worker can only be chosen once.
# Return the total cost to hire exactly k workers.
# Example 1:
# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap = []
        right_heap = []
        left_pointer = 0
        right_pointer = len(costs) - 1
        while left_pointer < len(costs) and left_pointer < candidates:
            heappush(left_heap, (costs[left_pointer], left_pointer))
            left_pointer += 1
        while right_pointer >= 0 and right_pointer >= len(costs) - candidates and right_pointer >= left_pointer:
            heappush(right_heap, (costs[right_pointer], right_pointer))
            right_pointer -= 1
        total_cost = 0
        for _ in range(k):
            if left_heap and right_heap:
                if left_heap[0][0] <= right_heap[0][0]:
                    cost, index = heappop(left_heap)
                else:
                    cost, index = heappop(right_heap)
            elif left_heap:
                cost, index = heappop(left_heap)
            else:
                cost, index = heappop(right_heap)
            total_cost += cost 
            if index < left_pointer:  
                if left_pointer < len(costs) and left_pointer <= right_pointer:
                    heappush(left_heap, (costs[left_pointer], left_pointer))
                    left_pointer += 1
            else:  
                if right_pointer >= 0 and right_pointer >= left_pointer:
                    heappush(right_heap, (costs[right_pointer], right_pointer))
                    right_pointer -= 1
        return total_cost
