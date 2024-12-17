class Solution(object):
    def countAndSay(self, n):
        res = '1'
        for i in range(n-1):
            res = self.count(res)
        return res




    def count(self,s):
        res = ''
        j = 0
        for i in range(1,len(s)):
            if s[j] != s[i]:
                res += str(i-j)
                res += s[j]
                j = i
        res += str(len(s) - j)  # Count of the last group
        res += s[j]  # The character itself
        return res

       

    
        
        