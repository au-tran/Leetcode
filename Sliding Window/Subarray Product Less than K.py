class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0 
        
        runningProduct = 1
        left = 0
        count = 0
        
        for i in range(len(nums)):
            runningProduct *= nums[i]
            
            while runningProduct >= k:
                runningProduct /= nums[left]
                left += 1 
            
            count += i - left + 1
            
        return count