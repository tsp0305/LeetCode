class Solution(object):
    def longestConsecutive(self, nums):
        nums= set(nums)
        d = {}
        s = [0]
        for i in nums:
            if (i-1) not in nums:
                d[i] = 1
                while (i+d[i]) in nums:
                    d[i] += 1
            s.append(d.get(i))
        return max(s)
            
                    
            
             



        