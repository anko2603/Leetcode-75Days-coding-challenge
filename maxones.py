# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_length = 0
        zero_count = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1

            
            max_length = max(max_length, end - start + 1)

        return max_length