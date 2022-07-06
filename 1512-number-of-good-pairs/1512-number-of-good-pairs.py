class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
            #j = i + 1
                if nums[i] == nums[j] and i <= j:
                    output += 1
        return output
                
        