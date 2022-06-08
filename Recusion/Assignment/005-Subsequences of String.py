# Time O(2 ^ n) | Space O(n)
def subsequences(str):
    result = []
    helper(str, 0, [], result)
    return result

def helper(string, i, comb, result):
    if i == len(string) and comb:
        result.append(''.join(comb))
        return
    
    if i >= len(string):
        return
    
    helper(string, i + 1, comb + [string[i]], result)
    helper(string, i + 1, comb, result)