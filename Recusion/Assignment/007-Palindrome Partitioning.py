# Time O(N * (2^N)) | Space O(N)
def partition(s):
    result = []
    helper(s, 0, [], result)
    return result

def helper(s, i, comb, result):
    if i == len(s):
        result.append(comb)
        return
    
    for idx in range(i + 1, len(s) + 1):
        curString = s[i: idx]
        if isPalindrome(curString):
            helper(s, idx, comb + [curString], result)
    
def isPalindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1; right -= 1
    return True