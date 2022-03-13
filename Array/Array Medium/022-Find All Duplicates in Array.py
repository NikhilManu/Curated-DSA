# Time O(N) | Space O(1)

# Marking the index as negative since in the range [1, n]
def findDuplicates(nums):
    res = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            res.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
        
    return res