# Time O(N ^ 2) | Spcae O(N ^ 2)

def PascalTriangle(numRows):
    res = [[1], [1, 1]]
    for i in range(3, numRows + 1):
        cur = [1] * i
        for j in range(1, i - 1):
            cur[j] = res[-1][j - 1] + res[-1][j]
        
        res.append(cur)
        
    return res if numRows != 1 else [[1]]