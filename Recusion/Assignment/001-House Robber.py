# Time O(2 ^ n) | Space O(N)
def rob(nums):
    return helper(nums, 0)

def helper(nums, i):
    if i >= len(nums):
        return 0

    rob = nums[i] + helper(nums, i + 2)
    skip = helper(nums, i + 1)

    return max(rob, skip)

# Time O(N) | Space O(N)
def rob(nums):
    return dpHelper(nums, 0, {})

def dpHelper(nums, i, dp):
    if i >= len(nums):
        return 0

    if i in dp:
        return dp[i]

    rob = nums[i] + dpHelper(nums, i + 2, dp)
    skip = dpHelper(nums, i + 1, dp)

    dp[i] = max(rob, skip)
    return dp[i]

