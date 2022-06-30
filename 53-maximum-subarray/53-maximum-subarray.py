class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0 
        
        #if len(nums) <= 1:
         #   return nums
        
        for n in nums:
            currSum = max(n, currSum + n)
            maxSum = max(maxSum, currSum)
        return maxSum
         
        
        
        