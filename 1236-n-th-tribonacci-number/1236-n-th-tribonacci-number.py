class Solution(object):
    def tribonacci(self, n):
        n1 = 0
        n2 = 1
        n3 = 1
        t = 0
        if n == 1 or n == 2:
            return 1
        for i in range(n-2):
            t = n1 + n2 + n3
            n1 = n2 
            n2 = n3
            n3 = t
        return t
        