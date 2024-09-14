class Solution(object):
    def findMiddleIndex(self, nums):
        ts = 0
        for i in nums:
            ts += i

        sum1= 0
        for i in range(len(nums)):
            sum2 = ts - sum1 - nums[i]
            if sum2 == sum1 :
                return i
            sum1 += nums[i]
        return -1
        
        