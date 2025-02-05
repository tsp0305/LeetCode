class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        i , sol , curr , n = 0 ,0 ,0, len(nums)
        while i < n:
            if nums[i] == 1:
                curr += 1
            elif nums[i] == 0:
                sol = max(curr,sol)
                curr = 0
            i += 1
        return max(sol,curr)
        