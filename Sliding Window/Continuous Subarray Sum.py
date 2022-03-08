class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        
        table = {0:-1}
        runningSum = 0

        for i in range(len(nums)):
            runningSum += nums[i]
            
            if runningSum % k not in table:
                table[runningSum % k] = i 
            
            if runningSum % k in table and i - table[runningSum % k] >= 2:
                return True
           
        return False
        
        
S = Solution()
nums = [23,2,4,6,7]
k = 6
print(S.checkSubarraySum(nums, k))

nums = [23,2,6,4,7]
k = 6
print(S.checkSubarraySum(nums, k))

nums = [23,2,6,4,7]
k = 13
print(S.checkSubarraySum(nums, k))

nums = [5,0,0,0]
k = 3
print(S.checkSubarraySum(nums, k))