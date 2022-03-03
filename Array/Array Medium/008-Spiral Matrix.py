# Time O(N) | Space O(N)

def SpiralMatrix(matrix):
    rbeg, rend, cbeg, cend = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    res = []
    while rbeg <= rend and cbeg <= cend:
        for i in range(cbeg, cend + 1):
            res.append(matrix[rbeg][i])
        rbeg += 1
        
        for i in range(rbeg, rend + 1):
            res.append(matrix[i][cend])     
        cend -= 1
        
        if rbeg <= rend:
            for i in reversed(range(cbeg, cend + 1)):
                res.append(matrix[rend][i])
            rend -= 1
        
        if cbeg <= cend:
            for i in reversed(range(rbeg, rend + 1)):
                res.append(matrix[i][cbeg])
            cbeg += 1
            
    return res