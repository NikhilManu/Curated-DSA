# Time O(2^N) | Space O(N * 2^N)

def combSum(arr, b):
    result = []
    helper(arr, 0, 0, b, [], result)
    return result

def helper(arr, i, curSum, b, comb, result):
    if curSum == b:
        result.append(comb)
        return 
    
    if i >= len(arr) or curSum > b:
        return
    
    helper(arr, i, curSum + arr[i], b, comb + [arr[i]], result)
    helper(arr, i + 1, curSum, b, comb, result)