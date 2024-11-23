# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        length = len(flowerbed)
        count = 0
        
        for i in range(length):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or out of bounds
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                
                # If both conditions are satisfied, plant a flower
                if prev_empty and next_empty:
                    flowerbed[i] = 1  # Mark the current plot as planted
                    count += 1  # Increment the planted flower count
                    if count >= n:
                        return True  # Early exit if enough flowers are planted
                    
        return count >= n 