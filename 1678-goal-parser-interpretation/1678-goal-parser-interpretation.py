class Solution:
    def interpret(self, command: str) -> str:
        result = ''
        #command = list(command)

        for i, el in enumerate(command):
            if el == 'G':
                result += 'G'
            elif el == '(' and command[i + 1] == ')':
                result += 'o'
            elif el == '(' and command[i + 1] == 'a':
                result += 'al'

        return result