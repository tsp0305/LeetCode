class Solution(object):
    def arrayRankTransform(self, arr):
        s = []
        s = sorted(arr)
        d = {}
        sol = []
        rank = 1
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = rank
                rank += 1
        for i in arr:
            sol.append(d.get(i))
        return sol

     
                    
        
        