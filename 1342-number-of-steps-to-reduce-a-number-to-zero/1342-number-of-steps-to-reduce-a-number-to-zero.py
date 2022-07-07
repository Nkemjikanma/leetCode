class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num:
            if num%2 != 0:
                num -= 1
                counter += 1
            else:
                num = num / 2
                counter += 1
        return counter

        
        