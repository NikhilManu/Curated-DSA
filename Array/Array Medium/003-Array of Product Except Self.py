# Time O(N) | Space O(N)

# Two Pass
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

# Single Pass
def productExceptSelf(nums):
    res = [1] * len(nums)
    leftRunningProduct, rightRunningProduct = 1, 1
    for i in range(len(nums)):
        res[i] *= leftRunningProduct
        leftRunningProduct *= nums[i]
        res[len(nums) - i - 1] *= rightRunningProduct
        rightRunningProduct *= nums[len(nums) - i - 1]

    return res