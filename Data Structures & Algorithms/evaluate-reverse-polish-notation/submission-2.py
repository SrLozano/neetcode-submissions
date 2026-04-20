class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif tokens[i] == '-':
                result = stack.pop() - stack.pop()
                stack.append(result)
            elif tokens[i] == '*':
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif tokens[i] == '/':
                result = stack.pop() / stack.pop()
                stack.append(result)
            else:
                stack.append(int(tokens[i]))

        return int(result)