from collections import Counter
import sys


# Keep count of letter in substring as you iterate 
# When substring has enough letter as required, try to shorten it 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Count number of letters in s & t 
        # If count of t is larger than found in s, there is no substring that matches requirement return empty string
        
        count1 = Counter(s)
        count2 = Counter(t)
        
        for elem in count2:
            if count2[elem] > count1[elem]:
                return ""
        
        
        # Window to keep track of letter count 
        # Need = length of t counter, number of unique characters in t 
    
        window = {i:0 for i in s}
        have, need = 0, len(count2)
        
        res = ""
        minLen = sys.maxsize
        start = 0 
        
        for i in range(len(s)):
            
            # Increase count of letter  
            window[s[i]] += 1 
            
            # If count of letter in substring is equal to count in t, have += 1 
            if window[s[i]] == count2[s[i]]:
                have += 1 
            
            # Found a substring, now try to shorten it by removing letters from start 
            while have == need:
                
                # If this substring is shorter than previously found, update result string and minLen 
                if i - start + 1 < minLen:
                       res = s[start:i+1]
                       minLen = i - start + 1
                       
                window[s[start]] -= 1 
                
                # If letter at start index is in count of t and now count of letters in substring is less than count of t, have -= 1 
                if s[start] in count2 and window[s[start]] < count2[s[start]]:
                       have -= 1
                start += 1
        
        
        return res if minLen != sys.maxsize else ""
        
S = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(S.minWindow(s, t))
s = "a"
t = "a"
print(S.minWindow(s, t))
s = "a"
t = "aa"
print(S.minWindow(s, t))