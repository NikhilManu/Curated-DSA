# Tiem O(N) | Space O(N)

def minRemoveToMakeValid(s):
    string = list(s)
    stack = []
    for idx, char in enumerate(string):
        if char == '(':
            stack.append(idx)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                string[idx] = ''

    while stack:
        string[stack.pop()] = ''
        
    return ''.join(string)