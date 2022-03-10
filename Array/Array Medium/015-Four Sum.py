# Solution 1 - Sort and do threeSum with an outer Loop

# Solution 2 - do twoSum with hashtable, (can be done without sorting the given array by storing the 4Sums in a set)

# Solution 3 - Generalizing this Problem to Ksum
# Time O(N ^(k - 1)) | Space O(N)
def FourSum(nums, target):
    nums.sort()
    result = []
    kSum(nums, 0, len(nums) - 1, target, 4, [], result)
    return result

def kSum(nums, l, r, target, k, ansTillNow, result):
    if r - l + 1 < k or k < 2:
        return 

    if k == 2:
        twoSum(nums, l, r, target, ansTillNow, result)
    else:
        for i in range(l, r + 1):
            if i > l and nums[i] == nums[i - 1]:
                continue
            kSum(nums, i + 1, r, target - nums[i], k - 1, ansTillNow + [nums[i]], result)

def twoSum(nums, left, right, target, ansTillNow, result):
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            result.append(ansTillNow + [nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            right -= 1
        elif sum < target:
            left += 1
        else:
            right -= 1
