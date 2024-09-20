class Solution(object):
    def reverseString(self, s):
        n = len(s) - 1
        l = len(s) // 2
        for i in range(l):
            s[i] , s[n-i] = s[n-i] , s[i]
        return s

