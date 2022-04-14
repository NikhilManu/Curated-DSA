# Time O() } Space O()

def generateParantheses(n):
    res = []
    helper(n, 0, 0, [], res)
    return res

def helper(n, op, cl, comb, res):
    if op > n or op < cl:
        return
    
    if cl == n:
        res.append(''.join(comb))
        return
    
    helper(n, op + 1, cl, comb + ['('], res)
    helper(n, op, cl + 1, comb + [')'], res)