# Time O(N) | Space O(N)
def printSeries(n, k):
    result = []
    helper(n, k, result)
    return result

def helper(n, k, result):
    result.append(n)
    
    if n <= 0: return

    helper(n - k, k, result)
    result.append(n)