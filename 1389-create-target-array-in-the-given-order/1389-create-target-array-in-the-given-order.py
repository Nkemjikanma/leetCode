class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        pairs = list(zip(index, nums))
        for pair in (pairs):
            target.insert(pair[0], pair[1])

        return target
        