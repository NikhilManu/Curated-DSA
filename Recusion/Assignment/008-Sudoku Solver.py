# Naive Solution
# Time O(9 ^ K) | Space O(1)
def solveSudoku(sudoku):
    return solve(sudoku)

def solve(board):
    position = getEmptyPosition(board)
    if not position:
        return board
    i, j = position
    
    for num in range(1, 10):
        if isSafe(board, i, j, num):
            board[i][j] = num
            if solve(board):
                return board
            board[i][j] = 0
            
def isSafe(board, i, j, num):
    for row in range(9):
        if board[row][j] == num:
            return False
    
    for col in range(9):
        if board[i][col] == num:
            return False
        
    rowBox = (i // 3) * 3
    colBox = (j // 3) * 3
    for row in range(3):
        for col in range(3):
            rowStart = rowBox + row
            colStart = colBox + col
            if board[rowStart][colStart] == num:
                return False
    return True

def getEmptyPosition(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                return i, j
                