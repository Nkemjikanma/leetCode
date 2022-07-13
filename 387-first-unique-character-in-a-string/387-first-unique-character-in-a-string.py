class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        
        for letter in s:
            if letter not in dict: 
                dict.setdefault(letter, 1)
            else: 
                dict[letter] += 1
                
        for key, value in dict.items(): 
            if value == 1:
                return s.index(key)
            if value > 1:
                continue
        return -1 
        