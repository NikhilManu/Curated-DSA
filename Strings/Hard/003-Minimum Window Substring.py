# TIme O(S + T) | Space O(S + T)

def minWindow(s, t):
    target = Counter(t)
    targetCount = len(target) # Notice that we are not taking len(t)
    current = {}
    idx, left = [0, float('inf')], 0
    for right in range(len(s)):
        char = s[right]
        if char not in current:
            current[char] = 0
        current[char] += 1
        
        if char in target and current[char] == target[char]:
            targetCount -= 1
            
        while targetCount == 0 and left <= right: # targetCount == 0 means letters of t inside s, now we need to minimize the window
            idx = [left, right] if right - left < idx[1] - idx[0] else idx
            
            if s[left] in target and current[s[left]] == target[s[left]]:
                targetCount += 1
                
            current[s[left]] -= 1
            left += 1
            
    return s[idx[0]: idx[1] + 1] if idx[1] != float('inf') else '' 
            
def Counter(string):
    dic = {}
    for char in string:
        if char not in dic:
            dic[char] = 0
        dic[char] += 1
    return dic