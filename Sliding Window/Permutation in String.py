class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        def matches(arr1, arr2):
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            
            return True
        
        arr1 = [0 for i in range(26)]
        arr2 = [0 for i in range(26)]
        
        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1
    
        if matches(arr1,arr2):
            return True
        
        left = 0 
        for i in range(len(s1), len(s2)):
            arr2[ord(s2[i]) - ord('a')] += 1
            arr2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            if matches(arr1,arr2):
                return True
        
        
            
        return False
        

s1 = "abcdxabcde"
s2 = "abcdeabcdx"
S = Solution()
print(S.checkInclusion(s1, s2))