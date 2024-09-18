class Solution(object):
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            low = i + 1
            high = len(numbers)-1
            while low <= high:
                mid = ((high - low) // 2 )+ low
                if numbers[mid] == target-numbers[i]:
                    return [i+1,mid+1]
                elif numbers[mid] < target - numbers[i]:
                    low = mid + 1
                else:
                    high = mid -1
        return [-1,-1]
            
        