# Time O(N * M) | Space O(1) --> Not Accepted

def strStr(haystack, needle):
    for idx in range(len(haystack) - len(needle) + 1):
        if haystack[idx] == needle[0]:
            i, j = idx, 0
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1; j += 1
                
            if j == len(needle): return idx
            
    return -1