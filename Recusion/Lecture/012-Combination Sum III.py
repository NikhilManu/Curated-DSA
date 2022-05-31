# Time O(2^9) | Space O(K)
def combinationSum3(k, n):
    result = []
    helper(n, k, 1, 0, [], result)
    return result

def helper(n, k, i, curSum, comb, result):
    if curSum == n and len(comb) == k:
        result.append(comb)
        return
    
    if len(comb) > k or curSum > n or i > 9:
        return 
    
    helper(n, k, i + 1, curSum + i, comb + [i], result)
    helper(n, k, i + 1, curSum, comb, result)
    
    
        
