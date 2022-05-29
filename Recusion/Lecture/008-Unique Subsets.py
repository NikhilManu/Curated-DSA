# Time O(2 ^ N) | Space O(N) without considering result space
def uniqueSubsets(arr): 
    arr.sort()
    result = []
    findSubset(arr, 0, [], result)
    return result

def findSubset(arr, i, comb, result):
    if i >= len(arr):
        result.append(comb)
        return 
   
    findSubset(arr, i + 1, comb + [arr[i]], result)
    while i < len(arr) - 1 and arr[i] == arr[i + 1]: i += 1
    findSubset(arr, i + 1, comb, result)