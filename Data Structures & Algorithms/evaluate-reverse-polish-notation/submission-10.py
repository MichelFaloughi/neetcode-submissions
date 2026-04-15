class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ["1","2","+","3","*","4","-"]

        stack = []

        for elem in tokens:
            if elem == '+':
                stack.append(stack.pop() + stack.pop())
            elif elem == '-':        
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif elem == '*':        
                stack.append(stack.pop() * stack.pop())
            elif elem == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else: # a number:
                elem = int(elem)
                stack.append(elem)
        
        return stack[-1]


       
