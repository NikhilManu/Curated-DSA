# Time O(2 ^ n) | Space O(n)

# Time O(N) | Space O(N)
def decodeWays(string):
    return helper(string, 0, {})

def helper(string, i, dp):
    if i == len(s):
        return 1

    if i in dp:
        return dp[i]

    if string[i] == '0': 
        return 0

    res = helper(string, i + 1, dp)

    if i + 1 < len(string) and string[i : i + 2] <= '26': # or int(string[i : i + 2] <= 26)
        res += helper(string, i + 2, dp)

    dp[i] = res
    return res


'''
At any point of time we have two choice
    1. take a single integer
    2. take current and next integer together if less than equal to 26
'''