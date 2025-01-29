# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
# Example 1:
# Input: a = 2, b = 6, c = 5
# Output: 3
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bitA, bitB, bitC = a & 1, b & 1, c & 1  
            if bitC == 0:
                flips += bitA + bitB  
            else:
                flips += (bitA | bitB) ^ 1 
                     
            a >>= 1
            b >>= 1
            c >>= 1
            
        return flips
