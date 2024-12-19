class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        res = 0
        for i in s:
            val = d.get(i,0) + 1
            d[i] = val
        c = 0
        for key,value in d.items():
            if value % 2 == 0:
                res += value
            elif value % 2 != 0 and c == 0:
                c += 1
                res += value
            elif value % 2 != 0:
                res += value - 1

            
        return res
            


        