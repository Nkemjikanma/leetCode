class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        maxVal = max(nums)
        
        for elem in nums: 
            if elem == maxVal:
                continue
            if (maxVal < (2 * elem)):
                return -1
            
        return nums.index(maxVal)
        
        
        
   