# Time O(N * M) | Space O(N * M)

def distintSubsequences(s, t):
    return dfs(s, t, 0, 0, {})

def dfs(s, t, i, j, cache):
    if j == len(t):
        return 1
    if i == len(s):
        return 0
    
    if (i, j) in cache:
        return cache[(i, j)]
    
    if s[i] == t[j]:
        cache[(i, j)] = dfs(s, t, i + 1, j + 1, cache) + dfs(s, t, i + 1, j, cache) # taking the current and also skipping the current
    else:
        cache[(i, j)] = dfs(s, t, i + 1, j, cache) # skip the current
        
    return cache[(i, j)]