# Time O(N!) | Space O(N^2)
def solveNQueens(n):
    result = []
    chessBoard = [[0 for i in range(n)] for j in range(n)]
    helper(0, n, chessBoard, result)
    return result

def helper(i, n, chessBoard, result):
    if i == n:
        current = []
        for row in chessBoard:
            for val in row:
                current.append(val)
        result.append(current)
        return 
    
    for j in range(n):
        if isSafe(i, j, n, chessBoard):
            chessBoard[i][j] = 1
            helper(i + 1, n, chessBoard, result)
            chessBoard[i][j] = 0
    
def isSafe(i, j, n, chessBoard):
    # UP
    row = i
    while row >= 0:
        if chessBoard[row][j] == 1:
            return False
        row -= 1
    
    # Right DIagonal
    row, col = i, j
    while row >= 0 and col <= n - 1:
        if chessBoard[row][col] == 1:
            return False
        row -= 1; col += 1
    
    # Left Diagonal
    row, col = i, j
    while row >= 0 and col >= 0:
        if chessBoard[row][col] == 1:
            return False
        row -= 1; col -= 1
        
    return True

'''
We can optimize this by removing the isSafe Method.

Functions done in isSafe Method

    1. Check if same column contains a another Queen.
        For this we need a array[n] where each indices determine the column Number. So we can mark it as occupied.
    2. Check if Right Diagonal contains another Queen.
        here eqn --> r + c
        [
            [0, 1, 2, 3]
            [1, 2, 3, 4]
            [2, 3, 4, 5]
            [3, 4, 5, 6]
        ]
        
        Here we are getting all right diagonal values same. This achieved by adding the index of the current position.
        So we can use this to mark if any element is placed. Each diagonal can be represented as a index in 1D array
    3. Check if Left Diagonal contains another Queen.
        here eqn --> (r - c) + (n - 1)
        [
            [3, 2, 1, 0]
            [4, 3, 2, 1]
            [5, 4, 3, 2]
            [6, 5, 4, 3]
        ]
        Here all the right diagonals have the same value. So each diagonal can be represented as a index of 1D array

'''
# Time O(N!) | Space O(N)
def solveNQueens(n):
    column, leftDiagonal, rightDiagonal = [False] * n, [False] * (2*n), [False] * (2*n)
    chessBoard = [[0 for i in range(n)] for j in range(n)]

    result = []
    helper(0, n, chessBoard, result, column, leftDiagonal, rightDiagonal)
    return result

def helper(i, n, chessBoard, result, column, leftDiagonal, rightDiagonal):
    if i == n:
        current = []
        for row in chessBoard:
            for val in row:
                current.append(val)
        result.append(current)
        return 
    
    for j in range(n):
        if not column[j] and not leftDiagonal[i - j + n - 1] and not rightDiagonal[i + j]:
            chessBoard[i][j] = 1
            column[j] = leftDiagonal[i - j + n - 1] = rightDiagonal[i + j] = True

            helper(i + 1, n, chessBoard, result, column, leftDiagonal, rightDiagonal)

            # undo the Change
            chessBoard[i][j] = 0
            column[j] = leftDiagonal[i - j + n - 1] = rightDiagonal[i + j] = False
        
        
    
    
    
    
    
    

        
    
    
    
    
    
    
