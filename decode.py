# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
    
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char == '[':
                   
                stack.append((current_str, current_num))
                current_str, current_num = "", 0
            elif char == ']':
                last_str, num = stack.pop()
                current_str = last_str + current_str * num
            else:
            
                current_str += char
    
        return current_str


        
