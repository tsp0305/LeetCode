class Solution(object):
    def maxSubArray(self, nums):
        maxs = nums[0]
        sums = 0
        for i in nums:
            sums += i
            maxs = max(maxs,sums)
            if sums < 0:
                sums = 0
            

        return maxs

        