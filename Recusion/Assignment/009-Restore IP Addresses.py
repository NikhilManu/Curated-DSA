# Time O() | Space O(1) | Having
def generateIPAddress(s):
    result = []
    helper(s, 0, [], result)
    return result

def helper(s, i, comb, result):
    if i == len(s) and len(comb) == 4:
        result.append('.'.join(comb))
        return 
    
    if len(comb) == 4 or i == len(s):
        return 
    
    for idx in range(i + 1, min((i+1) + 3, len(s) + 1)): # we can only take i to i + 3 characters at max in a single position
        strNum = s[i: idx]
        num = int(strNum)
        if num > 255 or len(strNum) > len(str(num)):
            return
        
        helper(s, idx, comb + [strNum], result)