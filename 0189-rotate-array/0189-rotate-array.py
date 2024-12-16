class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        self.reverse(0,n-k-1,nums)
        self.reverse(n-k,len(nums)-1,nums)
        self.reverse(0,len(nums)-1,nums)

        

    def reverse(self,i,j,nums):
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        return nums

        
        