class Solution:
    def isValid(self, s: str) -> bool:
        
        # " [ ( ] ) "
        #.      ^
        # < [          >

        # init empty stack []
        # for b in s
        # if open bracket, append/push to stack
        # else, pop, check if they match
        #   if they don't -> false
        #
        # after loop, return stack == []
              
        stack = []

        for b in s:
            if b in ["(", "[", "{"]:
                stack.append(b)
            elif stack == []:
                return False
            else:
                o = stack.pop()
                if not (
                    (o == '(' and b == ')')
                or (o == '[' and b == ']')
                or (o == '{' and b == '}')
                ):
                    return False

        return stack == []
        
        