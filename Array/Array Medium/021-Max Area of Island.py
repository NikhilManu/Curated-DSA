# Time O(N * M) | Space O(N * M)

def maxArea(grid):
    maxArea, seen = 0, set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                maxArea = max(maxArea, dfs(grid, i, j, seen)) 
                #maxArea = max(maxArea, iterativeDfs(grid, i, j, seen))
    
    return maxArea
        

def dfs(grid, i, j, seen):
    if outOfBounds(grid, i, j) or (i,j) in seen or grid[i][j] == 0:
        return 0
    
    seen.add((i,j))
    return 1 + dfs(grid, i + 1, j, seen) + dfs(grid, i - 1, j, seen) + dfs(grid, i, j + 1, seen) + dfs(grid, i, j - 1, seen)

def iterativeDfs(grid, i, j, seen):
    stack = [(i, j)]
    area = 0
    while stack:
        i, j = stack.pop()
        
        if outOfBounds(grid, i, j) or (i,j) in seen or grid[i][j] == 0:
            continue
        
        seen.add((i, j))
        area += 1
        stack.append((i + 1, j))
        stack.append((i - 1, j))
        stack.append((i, j + 1))
        stack.append((i, j - 1))
    
    return area
    
def outOfBounds(grid, i, j):
    return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i])