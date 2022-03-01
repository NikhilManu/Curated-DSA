# Time O(N) | Space O(1)

# Imagine this as balance scale with all the weights on right side of the 
# scale, you just have to remove each one and check if it balances, the balancing 
# point is the pivot
def pivotIndex(nums):
    totalSum, curSum = sum(nums), 0
    for idx, num in enumerate(nums):
        totalSum -= num
        if totalSum == curSum:
            return idx
        curSum += num
        
    return -1