# Time O(S) | Space O(1) -> where S is sum of all strings

# Prefix can only be atmost the shortest string inside the array
def longestCommonPrefix(strs):
    if not strs: return ''
    prefix = strs[0] # Can find the shortest string in array 
    for string in strs:
        while prefix and prefix != string[:len(prefix)]:
            prefix = prefix[:len(prefix) - 1] 
            
    return prefix

