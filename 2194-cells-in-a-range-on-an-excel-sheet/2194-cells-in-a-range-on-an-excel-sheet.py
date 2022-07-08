class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1, row1, col2, row2 = ord(s[0]), int(s[1]), ord(s[3]), int(s[4])
        
        output = []
        
        for col in range(col1, col2 + 1):
            for row in range(row1, row2 + 1):
                output.append(chr(col) + str(row))
                
        return output