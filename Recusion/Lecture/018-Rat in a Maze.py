# Time O(4^(m * n)) | Space O(m * n)

def searchMaze(arr, n):
    result = []
    helper(arr, 0, 0, [], result)
    return result
    
def helper(arr, i, j, comb, result):
    if i == len(arr) - 1 and j == len(arr[i]) - 1:
        result.append(''.join(comb))
        return
    
    if outOfBounds(arr, i, j) or arr[i][j] == 0:
        return
    
    arr[i][j] = 0
    helper(arr, i - 1, j, comb + ['U'], result)
    helper(arr, i + 1, j, comb + ['D'], result)
    helper(arr, i, j + 1, comb + ['R'], result)
    helper(arr, i, j - 1, comb + ['L'], result)
    arr[i][j] = 1
        
def outOfBounds(arr, i, j):
    return i < 0 or j < 0 or i >= len(arr) or j >= len(arr[i])
   