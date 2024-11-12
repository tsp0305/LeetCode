class Solution(object):
    def rob(self, nums):
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob1 = 0
        rob2 = 0
        temp = 0
        for i in nums:
            temp = max(rob1+i,rob2)
            rob1 = rob2
            rob2 = temp
        return temp
        