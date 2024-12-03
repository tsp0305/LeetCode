class Solution(object):
    def mergeAlternately(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1,n2)
        res = ''
        i,j = 0,0
        while i < n:
            res += word1[i]
            res += word2[i]
            i+=1
        if n2 < n1:
            while i < n1:
                res += word1[i]
                i += 1
        else:
            while i < n2:
                res += word2[i]
                i += 1
        return res
        


        
        