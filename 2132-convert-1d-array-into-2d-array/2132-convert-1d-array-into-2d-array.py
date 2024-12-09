class Solution(object):
    def construct2DArray(self, original, m, n):
        if m*n != len(original):
            return []
        arr = [[0] * n for _ in range(m)]
        n1 = len(original)
        k = 0
        for i in range(m):
            for j in range(n):
                arr[i][j] = original[k]
                k += 1
        return arr

                


        