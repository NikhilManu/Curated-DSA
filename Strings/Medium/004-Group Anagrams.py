# Time O(N * log(M)) | Space O(N)

def groupAnagrams(strs):
    groups = {}
    for string in strs:
        sortedString = str(sorted(string))
        if sortedString not in groups:
            groups[sortedString] = []
            
        groups[sortedString].append(string)
        
    res = []
    for key in groups:
        res.append(groups[key])
        
    return res