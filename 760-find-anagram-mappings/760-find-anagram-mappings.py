class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [] 
        for i in range(len(nums1)): 
            output.append(nums2.index(nums1[i]))
        
        return output