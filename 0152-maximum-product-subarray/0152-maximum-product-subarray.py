class Solution(object):
    def maxProduct(self, nums):
        mx = nums[0]
        mn = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            temp = max(mx * nums[i], nums[i] , mn * nums[i])
            mn = min (mx*nums[i] , nums[i] , mn * nums[i])
            mx = temp

            res = max (mx,res)
        return res

        