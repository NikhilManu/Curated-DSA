# Time O(2^N) | Space O(N * 2^N)
def combinationSumII(arr, target):
    arr.sort()
    result = []
    helper(arr, target, 0, 0, [], result)
    return result

def helper(arr, target, i, curSum, comb, result):
    if curSum == target:
        result.append(comb)
        return
    
    if i >= len(arr) or curSum > target:
        return

    helper(arr, target, i + 1, curSum + arr[i], comb + [arr[i]], result)
    while i + 1 < len(arr) and arr[i] == arr[i + 1]: i += 1
    helper(arr, target, i + 1, curSum, comb, result)