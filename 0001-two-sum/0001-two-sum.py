class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            x = target - nums[i]
            t = d.get(x,-1) 
            if  t != -1:
                return [i,t]
            d[nums[i]] = i
        

        
            
            
        
            
            

        
        