class Solution:
    def clumsy(self, n: int) -> int:
        
        stack = [n]
        operation = 1
        
        for i in range(n-1, 0, -1):
            operation %= 4
            
            if operation == 1: stack[-1] *= i
                
            elif operation == 2: stack[-1] = int(stack[-1] / i)
            
            elif operation == 3: stack.append(+i)
                
            else: stack.append(-i)
                
            operation += 1
        
       
        return sum(stack)
        