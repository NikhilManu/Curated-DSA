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


# Time O(MN) | Space O(A) -- where A is the number of alive nodes

#Infinite Board Solution
def gameOfLife(board):
    directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
    alive = getAliveIdx(board)
    
    count = {}
    for i, j in alive:
        for x, y in directions:
            if (i + x, j + y) not in count:
                count[(i + x, j + y)] = 0
            count[(i + x, j + y)] += 1
            
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) not in count:
                board[i][j] = 0
                continue
                
            if count[(i, j)] == 3 and board[i][j] == 0:
                board[i][j] = 1
            if count[(i, j)] not in [2, 3] and board[i][j] == 1:
                board[i][j] = 0
                
    
def getAliveIdx(board):
    alive = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                alive.add((i, j))
                
    return alive

"""
The Idea in the Last Solution is that the board is infinite.

 -> So we take the points which are alive
 -> then we keep count of alive for neighbours and the current node
 -> In the last step, we just find the take the conditions for dead --> alive and vice versa 
"""
