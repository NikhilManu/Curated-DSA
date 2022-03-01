# Time O(N ^ 2) | Space O(N ^ 2)

def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        # To avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            target = nums[i] + nums[left] + nums[right]
            if target == 0:
                res.append([nums[i], nums[left], nums[right]])
                # avoids duplicate 
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # avoids duplicate 
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1; right -= 1
            elif target < 0:
                left += 1
            else:
                right -= 1
    return res