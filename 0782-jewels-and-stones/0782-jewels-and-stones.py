class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        sol = 0
        for i in stones:
            if i in jewels:
                sol += 1
        return sol
        