# Time O() | Space O()
def present(board, word, n, m):
    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0] and helper(board, word, i, j, 0, set()):
                return True
    return False

def helper(board, word, i, j, k, seen):
    if k == len(word):
        return True
    
    if outOfBounds(board, i, j) or (i, j) in seen or board[i][j] != word[k]:
        return False
    
    seen.add((i, j))
    left = helper(board, word, i, j - 1, k + 1, seen)
    right = helper(board, word, i, j + 1, k + 1, seen)
    up = helper(board, word, i - 1, j, k + 1, seen)
    down = helper(board, word, i + 1, j, k + 1, seen)
    seen.remove((i, j))
    
    return left or right or up or down

def outOfBounds(board, i, j):
    return i < 0 or i >= len(board) or j < 0 or j >= len(board[i])
               