# Time O(4^n * n) | Space O(n)

dic = {'2': 'abc', '3': 'def','4': 'ghi', '5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}
def combinations(s):
    result = []
    helper(s, 0, [], result)
    return result

def helper(s, i, comb, result):
    if len(comb) == len(s):
        result.append(''.join(comb))
        return 
    
    if i == len(s) or len(comb) > len(s):
        return
    
    for char in dic[s[i]]:
        helper(s, i + 1, comb + [char], result)