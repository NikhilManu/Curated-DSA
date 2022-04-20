# Time O(N) | Space O(N)

def simplifyPath(path):
    path = path.split('/')
    res = ['']
    for word in path:
        if word == '' or word == '.':
            continue
            
        if word == '..':
            if res[-1] != '':
                res.pop()
        else:   
            res.append(word)
        
    return '/' if len(res) == 1 else '/'.join(res)