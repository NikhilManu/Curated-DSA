# Tiem O(MN) | Space O(MN)

# Not Acceptable in Interview
directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
def gameOfLife(board):
        dic = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    checkNeighbours(board, dic, i, j, False)
                else:
                    checkNeighbours(board, dic, i, j, True)
                    
def checkNeighbours(board, dic, i, j, alive):
    count = 0
    for x, y in directions:
        if not outOfBound(board, i + x, j + y):
            count += wasAlive(board, dic, i + x, y + j)
    
    if not alive:
        dic[(i, j)] = 0    
        if count == 3:
            board[i][j] = 1
    else:
        dic[(i, j)] = 1
        if count < 2 or count > 3:
            board[i][j] = 0

def wasAlive(board, dic, i, j):
    if (i, j) not in dic:
        return board[i][j]
    return dic[(i, j)]
    
def outOfBound(board, i, j):
    return i < 0 or j < 0 or i >= len(board) or j >= len(board[i])


# Time O(MN) | Space O(1) - Accepted

# dead --> dead --> 0
# alive --> alive --> 1
# dead --> alive --> 2
# alive --> dead --> -1
def gameofLife(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            modifyBoard(board, i, j)

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 1 if board[i][j] > 0 else 0
    
def modifyBoard(board, i, j):
    count = 0
    for x, y in directions:
        if not outOfBound(board, i + x, j + y) and abs(board[i + x][j + y]) == 1:
            count += 1
    
    if board[i][j] == 0 and count == 3:
        board[i][j] = 2
    if board[i][j] == 1 and (count < 2 or count > 3):
        board[i][j] = -1

def outOfBound(board, i, j):
    return i < 0 or j < 0 or i >= len(board) or j >= len(board[i])


