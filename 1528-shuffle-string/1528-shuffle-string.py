class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        pairs = list(zip(indices, s))
        pairs = sorted(pairs)
        output = ''

        for pair in pairs:
            output += pair[1]

        #output = ''.join(output)
        return output