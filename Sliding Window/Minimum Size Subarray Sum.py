import sys

class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        
        runningSum = 0 
        start = 0 
        minLen = sys.maxsize
        
        for i in range(len(nums)):
            runningSum += nums[i]
            
            while runningSum >= target:
                if i - start + 1 < minLen:
                    minLen = i - start + 1
                runningSum -= nums[start]
                start += 1
            
            
        return 0 if minLen == sys.maxsize else minLen

S = Solution()


target = 7
nums = [2,3,1,2,4,3]
print(S.minSubArrayLen(target, nums))
target = 4
nums = [1,4,4]
print(S.minSubArrayLen(target, nums))
target = 11
nums = [1,1,1,1,1,1,1,1]
print(S.minSubArrayLen(target, nums))