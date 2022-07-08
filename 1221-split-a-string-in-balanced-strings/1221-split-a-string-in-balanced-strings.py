class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        output = []
        
        for letter in s:
            if letter == 'R':
                l += 1
            elif letter == 'L':
                r += 1
            
            if r == l:
                output.append(r)
                r = 0
                l = 0
        return len(output)
        
