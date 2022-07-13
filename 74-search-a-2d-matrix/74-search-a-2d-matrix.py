class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid_index = (lo + hi) // 2
            mid_value = matrix[mid_index]

            if target in mid_value:
                return True
            #else:
                #for value in mid_value:
            if target < min(mid_value):
                hi = mid_index - 1
            else:
                lo = mid_index + 1

        return False