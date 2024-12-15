# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")  
        max_count = 0
        current_count = 0
        
        
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_count = current_count
        
        
        for i in range(k, len(s)):
            
            if s[i] in vowels:
                current_count += 1
            
            if s[i - k] in vowels:
                current_count -= 1
           
            max_count = max(max_count, current_count)
        
        return max_count
        
