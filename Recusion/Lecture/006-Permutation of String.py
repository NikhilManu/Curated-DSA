# Time O(N * N!) | Space O(N) if result Array is excluded
def permutation(string):
    result = []
    permutationHelper(list(string), 0, result)
    return result

def permutationHelper(string, pos, result):
    if pos >= len(string):
        result.append(''.join(string))
        return 
    
    for i in range(pos, len(string)):
        swap(string, pos, i)
        permutationHelper(string, pos, i + 1)
        swap(string, pos, i)

def swap(array, posA, posB):
    array[posA], array[posB] = array[posB], array[posA]