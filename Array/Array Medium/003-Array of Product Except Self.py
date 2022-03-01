# Time O(N) | Space O(N)

def productExceptSelf(nums):
    res = [1] * len(nums)
    leftRunningProduct = 1
    for i in range(1, len(nums)):
        leftRunningProduct *= nums[i - 1]
        res[i] = leftRunningProduct

    rightRunningProduct = 1
    for i in reversed(range(len(nums) - 1)):
        rightRunningProduct *= nums[i + 1]
        res[i] *= rightRunningProduct

    return res