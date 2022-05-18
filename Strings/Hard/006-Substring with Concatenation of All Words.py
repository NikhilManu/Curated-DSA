# Time O() | Space O()

def findSubstring(s, words):
    dic = {} 
    for word in words:
        if word not in dic:
            dic[word] = 0
        dic[word] += 1
        
    res = []    
    k = len(words[0])
    WordMissing, substringLength = len(words), k * len(words) 
    for i in range(len(s) - substringLength + 1):
        cur = dic.copy()
        missing = WordMissing 
        for idx in range(i, i + substringLength, k): 
            word = s[idx: idx + k]
            if word in cur and cur[word] > 0:
                cur[word] -= 1
                missing -= 1
            else:
                break
                
        if not missing:
            res.append(i)
            
    return res

def findSubString(s, words):
    dic = {}
    for word in words:
        if word not in dic:
            dic[word] = 0
        dic[word] += 1
        
    k, res = len(words[0]), []
    # we use k as the range because, there is no we can check for the immediate k indices after we found a word
    # as we are skipping by k indices
    # [foo, bar], let say we encounter [f o o], we also need to iterate from 2nd O and also 3rd o
    for i in range(k):
        counter = dic.copy()
        start, end, count = i, i, len(words)
        while end < len(s):
            word = s[end: end + k]
            if word in counter:
                counter[word] -= 1
                if counter[word] >= 0:
                    count -= 1
            end += k
            
            if count == 0:
                res.append(start)
                
            if end - start == k * len(words):
                word = s[start: start + k]
                if word in counter:
                    counter[word] += 1
                    if counter[word] > 0:
                        count += 1
                start += k
                
    return res               