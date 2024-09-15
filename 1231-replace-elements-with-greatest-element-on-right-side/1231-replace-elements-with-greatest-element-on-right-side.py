class Solution(object):
    def replaceElements(self, arr):
        high = arr[-1]
       
        for i in range(len(arr)-2,-1,-1):
            temp = arr[i]
            
            arr[i] = high
            if temp > high:
                high = temp
           
            
        arr[-1] = -1
        return arr


        