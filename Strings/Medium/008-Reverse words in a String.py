# Time O(N) | Space O(N)

def reverseWords(s):
    i, res = 0, []
    while True:
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i >= len(s): break
        
        j = i + 1
        while j < len(s) and s[j] != ' ':
            j += 1
            
        res = [s[i:j]]+ res if s[i:j] else res
        
        if j >= len(s): break
        
        i = j + 1
        
    return ' '.join(res)