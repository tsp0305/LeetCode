class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 1
        r = x
        while l <= r:
            mid = (l + r )//2
            if x == mid * mid:
                return mid
            elif mid*mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
        