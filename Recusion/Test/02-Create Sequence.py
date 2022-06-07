# Time O(2 ^ D) | Space O(N)
def createSequence(n):
    result = []
    helper(n, 0, result)
    return result # Sorting required in some platforms

def helper(n, cur, result):
    if cur > n:
        return
    
    if cur != 0:
        result.append(cur)
    
    helper(n, cur * 10 + 2, result)
    helper(n, cur * 10 + 5, result)