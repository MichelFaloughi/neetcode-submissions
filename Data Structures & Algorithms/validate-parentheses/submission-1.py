class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if b in ['[', '(', '{']:
                stack.append(b)
            else: # b is closing
                if not stack: return False
                top = stack.pop()
                if not ( (top=='[' and b==']') or
                     (top=='{' and b=='}') or
                     (top=='(' and b==')')
                    ):
                    return False
        return not stack

    # "( [ { } ] ) ("
    #           ^

    # "[ ( ] )"
    #      ^

    # stack: [  