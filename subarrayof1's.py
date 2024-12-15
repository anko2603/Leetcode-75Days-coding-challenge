# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        zero_count = 0
        max_length = 0

        for end in range(len(nums)):

            if nums[end] == 0:
                zero_count += 1
            

            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            

            max_length = max(max_length, end - start)
        
        return max_length

        