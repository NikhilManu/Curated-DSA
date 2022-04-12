# Time O(N * M) | Space O(1) --> Not Accepted

def strStr(haystack, needle):
    for idx in range(len(haystack) - len(needle) + 1):
        if haystack[idx] == needle[0]:
            i, j = idx, 0
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1; j += 1
                
            if j == len(needle): return idx
            
    return -1

# Knuth Morris Pratt Algorithm  --> https://www.youtube.com/watch?v=JoF0Z7nVSrA
# Time O(N + M) | Space O(M)

def strStr(haystack, needle):
    pattern = buildLongestPrefixSuffixArray(needle)
    return KMP(haystack, needle, pattern)
    
def buildLongestPrefixSuffixArray(needle):
    prev, cur = 0, 1
    pattern = [0] * len(needle)
    while cur < len(needle):
        if needle[cur] == needle[prev]:
            pattern[cur] = prev + 1
            prev += 1; cur += 1
        elif prev == 0:
            pattern[cur] = 0
            cur += 1
        else:
            prev = pattern[prev - 1]
            
    return pattern 

def KMP(haystack, needle, pattern):
    i, j = 0, 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1; j += 1
        elif j == 0:
            i += 1
        else:
            j = pattern[j - 1]
            
        if j == len(needle):
            return i - len(needle)
        
    return -1