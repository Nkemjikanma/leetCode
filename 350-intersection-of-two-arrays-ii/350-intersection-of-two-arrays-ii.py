class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        nums1 = Counter(nums1)
        
        for n in nums2: 
            if nums1[n] > 0:
                result.append(n)
                nums1[n] -= 1
                
        return result

        