
def maxSubArrayEqualsK(nums, target):
    
    
    # Table initialized with 0:-1 
    # incase the runningSum is equals to the target 
    # so i - table[runningSum-target] becomes i - (- 1) -> i + 1
    table = {0: -1}
    runningSum = 0 
    maxLen = 0
    
    for i, value in enumerate(nums):
        runningSum += value 
        
        # Check if runningSum is not in table 
        # We store the 1st occurence of runningSum only 
        # because the 2nd, 3rd occurence onwards belong to a bigger subarray from 0 -> i 
        # that will reduces the length of i - table[runningSum-target]
        if runningSum not in table:
            table[runningSum] = i 
        
        if runningSum - target in table:
            maxLen = max(maxLen, i - table[runningSum-target])
        
    
    return maxLen
        
        


print(maxSubArrayEqualsK([1,2,3,4,5], 5))