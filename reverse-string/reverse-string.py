class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        loc = 0
        for i, j in reversed(list(enumerate(s))):
            s[loc] = j
            
            loc += 1 
            
        return s
        