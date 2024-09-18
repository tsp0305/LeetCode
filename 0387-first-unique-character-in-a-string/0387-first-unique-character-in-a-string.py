class Solution(object):
    def firstUniqChar(self, s):
        d = {}
        sol = []
        for i in range(len(s)):
            val = d.get(s[i],0) + 1
            d[s[i]] = val
        for i,a in enumerate(s):
            if d[a] == 1:
                return i

        return -1
            



        
        