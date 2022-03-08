class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        runningSum = 0 
        table = {0:1}
        count = 0
        
        for i in range(len(nums)):
            runningSum += nums[i]
            
            if runningSum % k not in table:
                table[runningSum % k] = 1 
            else:
                count += table[runningSum % k]
                table[runningSum % k] += 1
                
        return count