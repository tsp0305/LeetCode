class Solution(object):
    def countBits(self, n):
        sol = []
        for i in range(n+1):
            sol.append(self.hammingWeight(i))
        return sol


    def hammingWeight(self, n):
        num = n
        sol = 0
        while num != 0:
            rem = num % 2
            if rem == 1:
                sol += 1
            num = num // 2
        return sol

        