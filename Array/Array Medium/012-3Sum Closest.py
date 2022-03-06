# Time O(N ^ 2) | Space O(1)

from fileinput import close


def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == target:
                return currentSum

            if abs(target - currentSum) < abs(target - closest):
                closest = currentSum

            if currentSum < target:
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
            else:
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1

    return closest