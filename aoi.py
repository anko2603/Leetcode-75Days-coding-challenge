# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
# The algorithm for myAtoi(string s) is as follows:
# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.
# Example 1:
# Input: s = "42"
# Output: 42
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result *= sign

        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result

