class Solution(object):
    def climbStairs(self, n):
        n1 = 0
        n2 = 1
        for i in range(n):
            sum = n1 + n2
            n1 = n2
            n2 = sum
        return sum
        