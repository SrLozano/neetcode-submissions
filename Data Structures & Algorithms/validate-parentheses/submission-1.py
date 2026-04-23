class Solution:
    def isValid(self, s: str) -> bool:
        
        close_parentheses = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }

        stack = []

        for p in s:
            if p in close_parentheses:
                if not stack or stack.pop() == close_parentheses[p]:
                    return False
            else:
                stack.append(p)

        return not stack
