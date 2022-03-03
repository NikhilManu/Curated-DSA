# Solution Explanation --> https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

# Time O(N) } Space O(1)
def nextPermutation(nums):
    pivot = getPivotIdx(nums)
    
    if pivot == -1:
        nums.reverse()
        return
    
    idxToSwap = getIdxToSwapWithPivot(pivot, nums)
    swap(pivot, idxToSwap, nums)
    reverse(pivot, nums)

def getPivotIdx(nums):
    for i in reversed(range(len(nums) - 1)):
        if nums[i] < nums[i + 1]:
            return i    
    return -1

def getIdxToSwapWithPivot(start, nums):
    pivotValue, diff = nums[start], float('inf')
    for i in range(start, len(nums)):
        if abs(pivotValue - nums[i]) <= diff and nums[i] > pivotValue:
            idxToSwap = i
    return idxToSwap

def reverse(pivot, nums):
    left, right = pivot + 1, len(nums) - 1
    while left < right:
        swap(left, right, nums)
        left += 1; right -= 1

def swap(first, second, nums):
    nums[first], nums[second] = nums[second], nums[first]