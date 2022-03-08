class Solution:
    def subarraySum(self, nums, k: int) -> int:
        
        runningSum = 0 
        map = {0:1}
        count = 0 
        for i, value in enumerate(nums):
            runningSum += value
            
            if runningSum - k in map:
                count += map[runningSum-k]
                
            map[runningSum] = 1 + map.get(runningSum, 0)

                
        return count 
        


