class Solution(object):
    def intersect(self, nums1, nums2):
        d = {}
        sol = []
        for i in nums1:
            val = d.get(i,0) + 1
            d[i] = val
        for i in nums2:
            val = d.get(i,0)
            if val >=1:
                d[i] = val - 1
                sol.append(i)
        return sol
            
            
       
          


        