class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False 
        
        t_count = collections.Counter(t)
        s_count = collections.Counter(s)
        
        
        for k, v in t_count.items():
            if v != s_count[k]:
                return False

        return True
        """for n in s:
            if t_count[n] > 0:
                t_count[n] -= 1
            else:
                return False
        """