# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.
# For chosen indices i0, i1, ..., ik - 1, your score is defined as:
# The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
# Return the maximum possible score.
# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.
# Example 1:
# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        min_heap = []
        current_sum = 0  
        max_score = 0  
        for num2, num1 in pairs:
            
            heappush(min_heap, num1)
            current_sum += num1
            if len(min_heap) > k:
                current_sum -= heappop(min_heap)
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)
        
        return max_score
