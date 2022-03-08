class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_repeated_letter, maxLength = 0, 0 
        start = 0 
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1 
            else:
                count[s[i]] += 1 
            most_repeated_letter = max(most_repeated_letter, count[s[i]])
            
            while i - start + 1 > most_repeated_letter + k:
                count[s[start]] -= 1 
                start += 1
            maxLength = max(i - start + 1, maxLength)
                
        return maxLength
            
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.