class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        newl = []
        i = 0
        while i < len(nums):
            
            for j in range(nums[i]):
                newl.append(nums[i+1])
            i+=2
        return newl