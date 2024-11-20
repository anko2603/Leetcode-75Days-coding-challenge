# You’re given two strings, word1 and word2. The goal is to merge the strings in an alternating manner. If one string is longer, the extra letters should be added to the end.

# Here’s an example:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []
        i, j = 0, 0

        # Alternate between characters from both strings
        while i < len(word1) and j < len(word2):
            merged_string.append(word1[i])
            merged_string.append(word2[j])
            i += 1
            j += 1

        # Add remaining characters from the longer string
        merged_string.extend(word1[i:])
        merged_string.extend(word2[j:])
        
        return ''.join(merged_string)
# Test the mergeAlternately function
solution = Solution()

