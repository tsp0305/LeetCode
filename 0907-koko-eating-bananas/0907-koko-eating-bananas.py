def hr(piles,k):
        hr = 0
        for i in piles:
            hr += math.ceil(i/k)
        return hr

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = l + (r-l) // 2
            if hr(piles,mid) <= h:
                r = mid 
            elif hr(piles,mid) > h:
                l = mid + 1
            
        return l
        
    
        