# Time O(2 ^ N) | Space O(N) --> answer we generated is O(2 ^ N)
def combinations(n ,k):
    result = []
    helper(n, 1, k, [], result)
    return result

def helper(n, i, k, comb, result):
    if len(comb) == k:
        result.append(comb)
        return 
    
    if i > n and len(comb) + (n - i + 1) < k:
        return
    
    helper(n, i + 1, k, comb + [i], result)
    helper(n, i + 1, k, comb, result)


    '''
    Meaning --> len(comb) + (n - i + 1) < k

    k = 3 and N = 4

    So lets assume we skipped 1 and 2 

    so currently we are on i = 3, but actually we dont need to do any further work since we already know 
    we will not get the answer here since [3, 4] is only possible from here.

    so we will keep a check where will only proceed if ** len(comb) + remaining Number of ELements > k ** 
    '''