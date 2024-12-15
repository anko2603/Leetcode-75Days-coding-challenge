# You are given a string s, which contains stars *.
# In one operation, you can:
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
# Note:
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.
# Example 1:
# Input: s = "leet**cod*e"
# Output: "lecoe"
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()  
            else:
                stack.append(char)  
        
        return ''.join(stack) 
        