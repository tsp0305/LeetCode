class Solution(object):
    def calPoints(self, operations):
        st = []
        for i in operations:
            if i == '+':
                st.append(st[-1] + st[-2])

            elif i == 'D':
                st.append(2*st[-1])

            elif i == 'C':
                st.pop()

            else:
                st.append(int(i))
        return sum(st)


        
        