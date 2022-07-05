class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]]) # if i == 1; nums[nums[i]] = nums[2]
        
        return ans
            
        