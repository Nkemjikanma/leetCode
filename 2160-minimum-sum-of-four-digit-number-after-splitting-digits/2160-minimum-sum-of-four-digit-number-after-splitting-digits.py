class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(map(int, str(num)))
        num = sorted(num, reverse=True)
        
        ans = 0 
        pos = 0 
        
        for i in range(len(num)):
            if i%2 == 0:
                ans += num[i] * 10**pos
            else: 
                ans += num[i] * 10**pos
                pos +=1
        return ans
                
            
        