class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = None
        # edge case: less than 3 positions
        for i in range(0, len(tokens) - 2, 2):
            print(tokens[i])
            if tokens[i + 2] == '+':
                result = int(tokens[i]) + int(tokens[i + 1])
            elif tokens[i + 2] == '-':
                result = int(tokens[i]) - int(tokens[i + 1])
            elif tokens[i + 2] == '*':
                result = int(tokens[i]) * int(tokens[i + 1])
            elif tokens[i + 2] == '/':
                result = int(tokens[i]) / int(tokens[i + 1])
            tokens[i+2] = result


        return result