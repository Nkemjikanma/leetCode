class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            idx = len(digits) - 1 - i # move along the array starting from end 
            
            if digits[idx] == 9:
                digits[idx] = 0
                
            else: 
                digits[idx] += 1
                
                return digits
        
        return[1] + digits
        