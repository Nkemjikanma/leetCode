class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            dict[i] = 0

            for j in range(0, len(nums)):
                #dict.setdefault(nums[i], 0)
                if nums[i] > nums[j]:
                    dict[i] += 1

        return list(dict.values())
        