# Time O(2^n) | Space O(N)

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

# Time O(N) | Space O(N)
def fibo(n, memo = {1:1, 2:1}):
    if n in memo:
        return memo[n]

    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]

