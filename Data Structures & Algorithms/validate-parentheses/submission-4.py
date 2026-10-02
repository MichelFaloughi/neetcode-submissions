class Solution:
    def isValid(self, s: str) -> bool:

        closed_to_opened = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        for b in s:
            if b in ['(','[','{']:
                stack.append(b)
            elif not stack:
                return False
            else:
                o = stack.pop()
                if o != closed_to_opened[b]:
                    return False
        
        return stack == []

        
        
        
        
        
        
        
        # " ( [ { } ] ) [ "
        #         ^
        # stack = [ ( [ {         ]
        # c = stack.pop() -> '{'

        
        
        