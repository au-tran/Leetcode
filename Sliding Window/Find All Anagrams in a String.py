class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        def matches(arr1, arr2):
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            return True
        
        arr1 = [0 for i in range(26)]
        arr2 = [0 for i in range(26)]
        res = []
        for i in range(len(p)):
            arr1[ord(p[i]) - ord('a')] += 1
            arr2[ord(s[i]) - ord('a')] += 1
    
        if matches(arr1,arr2):
            res.append(0)
        
        left = 0 

        for i in range(len(p), len(s)):
            arr2[ord(s[i]) - ord('a')] += 1
            arr2[ord(s[left]) - ord('a')] -= 1
            left += 1
            if matches(arr1,arr2):
                res.append(left)
        
        return res
        

