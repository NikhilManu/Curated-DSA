# Time O(N) | Space O(N)
def reverseArray(arr, m):
    reverseHelper(arr, m + 1, len(arr) - 1)
    return arr

def reverseHelper(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverseHelper(arr, l + 1, r - 1)
