class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        minimum = float("inf")
        for price in prices:
            minimum = min(minimum, price)
            output = max(output, price - minimum)

        return output
        