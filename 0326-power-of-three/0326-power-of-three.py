class Solution(object):
    def isPowerOfThree(self, n):
        i = 0
        n1 = 1
        if n == 0 or n < 0 :
            return False
        while n1 <= n:
            n1 = 3 ** i
            i += 1
            if n == n1:
                return True
        return False


        