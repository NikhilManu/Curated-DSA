# Time O() | Space O()
def generate(n):
    result = []
    helper(n, 0, 0, [], result)
    return result

def helper(n, op, cl, comb, result):
    if op > n or cl > op:
        return 
    
    if cl == n:
        result.append(''.join(comb))
        return 
    
    helper(n, op + 1, cl, comb + ['('], result)
    helper(n, op, cl + 1, comb + [')'], result)