class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): 
            return False 
        
        
        magazine_count = collections.Counter(magazine)
        ransomNote_count = collections.Counter(ransomNote)
        
        for k, v in ransomNote_count.items(): 
            main_count = magazine_count[k]
            
            if main_count < v: 
                return False
            
        return True
        