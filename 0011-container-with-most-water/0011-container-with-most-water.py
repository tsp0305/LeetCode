class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        sol = 0
        while l<r:
            w = r - l
            ht = min(height[l],height[r])
            cw = w * ht
            sol = max(sol,cw)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return sol