# Time O(N) | Space O(N)

def sortedSquares(nums):
    res = [0] * len(nums)
    left, right, k = 0, len(nums) - 1, len(nums) - 1
    while left <= right:
        leftNum = nums[left] ** 2
        rightNum = nums[right] ** 2
        
        if leftNum > rightNum:
            res[k] = leftNum
            left += 1
        else:
            res[k] = rightNum
            right -= 1
            
        k -= 1
        
    return res