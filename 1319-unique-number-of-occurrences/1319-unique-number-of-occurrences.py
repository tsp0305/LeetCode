class Solution(object):
    def uniqueOccurrences(self, arr):
        d = {}
        s = []
        for i in arr:
            val = d.get(i,0) + 1
            if val == 1:
                s.append(i)
            d[i] = val
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if d[s[i]] == d[s[j]]:
                    return False
        return True
        
        