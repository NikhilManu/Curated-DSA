# Time O(N) | Space O(N)

# Just split House Robber into 2 Case: 1. 1 to n-1 and 2. 2 to n
def rob(nums):
    if len(nums) <= 2:
        return max(nums)

    return max(dpHelper(nums[:-1], 0, {}), dpHelper(nums[1:], 0, {}))

def dpHelper(nums, i, dp):
    if i >= len(nums):
        return 0

    if i in dp:
        return dp[i]

    rob = nums[i] + dpHelper(nums, i + 2, dp)
    skip = dpHelper(nums, i + 1, dp)

    dp[i] = max(rob, skip)
    return dp[i]