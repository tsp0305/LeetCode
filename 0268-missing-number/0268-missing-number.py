class Solution(object):
    def missingNumber(self, nums):
        n = len(nums) 
        s = n * (n+1) / 2 
        r = 0
        for i in nums:
            r += i


        return s - r
            
            

            


        