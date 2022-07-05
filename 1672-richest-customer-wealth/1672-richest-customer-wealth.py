class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        sumOf = 0
        for i in range(len(accounts)):
            sumOf = sum(accounts[i])
            richest = max(richest, sumOf)
        return richest
    
        