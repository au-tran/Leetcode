class Solution:
    def getAverages(self, nums, k: int):
        if k == 0:
            return nums
        if k > len(nums)//2:
            return [-1 for i in nums]
        avgs = [0 for i in nums]
        
        for i in range(k):
            avgs[i] = -1
            avgs[len(nums)-1 - i] = -1
            
        prefix_sums = [0 for i in nums]
        prefix_sums[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefix_sums[i] = nums[i] + prefix_sums[i-1]
            
        for i in range(k, len(nums) - k):
            if i-k-1 >= 0:
                avgs[i] = (prefix_sums[i+k] - prefix_sums[i-k-1]) // (k*2+1)
            else:
                avgs[i] = prefix_sums[i+k] // (k*2+1)
        
        
        return avgs
        
        
S = Solution()
nums = [7,4,3,9,1,8,5,2,6]
k = 3
print(S.getAverages(nums, k))

nums = [100000]
k = 0
print(S.getAverages(nums, k))
nums = [8]
k = 100000
print(S.getAverages(nums, k))

nums = [2,2,1]
k = 1
print(S.getAverages(nums, k))