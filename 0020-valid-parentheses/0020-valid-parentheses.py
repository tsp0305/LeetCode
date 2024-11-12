class Solution(object):
    def isValid(self, s):
        st = [-1]
        for i in s:
            st.append(i)
            if self.check(st[-2],i):
                st.pop()
                st.pop()
        if st[-1] == -1:
            return True
        return False
    def check(self,i,j):
        if (i == '{' and j == '}') or (i == '(' and j == ')') or (i == '[' and j== ']') :
            return True
        return False
        