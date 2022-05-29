# Time O(2^N) | Space O(N)
def pwset(arr):
    result = []
    helper(arr, 0, [], result)
    return result

def helper(arr, i, subset, result):
    if i >= len(arr):
        result.append(subset)
        return 
    helper(arr, i + 1, subset + [arr[i]], result) # Include
    helper(arr, i + 1, subset, result) # Not Include
