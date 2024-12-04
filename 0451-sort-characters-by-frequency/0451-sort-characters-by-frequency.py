class Solution(object):
    def frequencySort(self, s):
        d = {}
        res = ''
        for i in s:
            val = d.get(i,0) + 1
            d[i] = val
        sorte = sorted(d,key = d.get,reverse = True)
        for i in sorte:
            res += i * d[i]
        return res
        
            


            
        
        