class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict = {}
        current = 0

        for a in key.replace(" ", ""):
            if a not in dict:
                dict[a] = chr(current + ord('a'))
                current += 1


        ans = []
        for letter in message:
            if letter == " ":
                ans.append(" ")
            else:
                ans.append(dict[letter])
            
        return "".join(ans)