class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prodTotal = 1 
        sumTotal = 0 
        n = str(n)
        
        for i in n:
            prodTotal *= int(i)
            sumTotal += int(i)
            
        return prodTotal - sumTotal
        