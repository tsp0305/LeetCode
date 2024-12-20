class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = [-1]
        for i in s:
            stk.append(i)
            if stk[-1] == ')' and stk[-2] == '(':
                stk.pop()
                stk.pop()
        return len(stk) - 1
        


        