# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  
        
        res = 0
        negative = x < 0  
        x = abs(x)  
        while x != 0:
            digit = x % 10  
            x //= 10  
            if res > (INT_MAX - digit) // 10:
                return 0
            
            res = res * 10 + digit  
        return -res if negative else res  

