class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for b in s:
            if b in ['(', '[', '{']:
                stack.append(b)
            elif not stack:
                return False
            else:
                o = stack.pop()
                if not (
                    (o == '(' and b == ')') or
                    (o == '[' and b == ']') or
                    (o == '{' and b == '}')
                ):
                    return False

        return not stack

        
        
        