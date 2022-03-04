# Time O(M * N * (4^s)) | Space O(M * N)
# Time Complexity : https://cs.stackexchange.com/questions/96626/whats-the-big-o-runtime-of-a-dfs-word-search-through-a-matrix

def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if word[0] == board[i][j] and wordExist(board, word, i, j, 0, set()):
                return True 
    return False
                
def wordExist(board, word, i, j, k, vis):
    if k == len(word):
        return True
    
    if outOfBounds(board, i, j) or (i, j) in vis or board[i][j] != word[k]:
        return False
    
    k += 1
    vis.add((i, j))

    left = wordExist(board, word, i, j - 1, k, vis)
    right = wordExist(board, word, i, j + 1, k, vis)
    up = wordExist(board, word, i - 1, j, k, vis)
    down = wordExist(board, word, i + 1, j, k, vis)

    found = left or right or up or down 
    vis.remove((i, j))
    return found
    
def outOfBounds(board, i, j):
    return i < 0 or j < 0 or i >= len(board) or j >= len(board[0])