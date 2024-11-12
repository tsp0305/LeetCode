class Solution(object):
    def minCostClimbingStairs(self, cost):
        c1 = 0
        c2 = 0
        cost.append(0)
        for i in cost:
            temp = min(c1+i,c2+i)
            c1 = c2
            c2 = temp
        return temp
        