# Time O(N) | Space O(N)
# https://www.youtube.com/watch?v=Q2Tw6gcVEwc

def zigzagConversion(s, numRows):
    if numRows == 1: return s

    res = []
    for row in range(numRows):
        jump = (numRows - 1) * 2
        for i in range(row, len(s), jump):
            res.append(s[i])
            if row > 0 and row < numRows - 1:
                idx = i + (numRows - row - 1) * 2  # OR idx = i + jump - 2 * row
                if idx < len(s):
                    res.append(s[idx])

    return ''.join(res)


'''
 PAYPALISHIRING   
    
0    P     I    N
1    A   L S  I G
2    Y A   H R
3    P     I

Create the algorithm from this pattern
'''