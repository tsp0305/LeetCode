class Solution(object):
    def hammingWeight(self, n):
        num = n
        sol = 0
        while num != 0:
            rem = num % 2
            if rem == 1:
                sol += 1
            num = num // 2
        return sol
        