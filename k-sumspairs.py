# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter()
        operations = 0

        for num in nums:
            complement = k - num
            if count[complement] > 0:
                # Pair found
                operations += 1
                count[complement] -= 1
            else:
                # Add the current number to the hash map
                count[num] += 1

        return operations
        
