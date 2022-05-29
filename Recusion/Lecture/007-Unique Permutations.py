# Time O(N * N!) | Space O(N)
def uniquePermutations(arr):
    result = []
    permutationHelper(arr, 0, result)
    return result

def permutationHelper(arr, pos, result):
    if pos == len(arr):
        result.append(arr[:])
        return
    
    lookup = set()
    for i in range(pos, len(arr)):
        if arr[i] in lookup:
            continue
        lookup.add(arr[i])
        swap(arr, pos, i)
        permutationHelper(arr, pos + 1, result)
        swap(arr, pos, i)
        
def swap(array, pos, i):
    array[pos], array[i] = array[i], array[pos]