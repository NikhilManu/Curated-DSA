# Time O(2^N) | Space O(N) without Dp

# Time O(N) | Space O(N)
def climbingStairs(n):
    return helper(n, {0: 1, 1: 1}) % 1000000007

def helper(n, dp):
    if n in dp:
        return dp[n]
    
    dp[n] = helper(n - 1, dp) + helper(n - 2, dp)
    return dp[n]