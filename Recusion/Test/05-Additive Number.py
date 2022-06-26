# Time O(N^2) | Space O(N)
def isAdditiveNumber(num):
    for i in range(1, len(num)//2 + 1):
        first = num[:i]
        for j in range(i, len(num)):
            second = num[i:j]
            found = helper(first, second, num[j:])
            if found: return True
        
    return False

def helper(first, second, string):
    if not string: 
        return True
    
    if not valid(first) or not valid(second):
        return False
    
    curSum = addString(first, second)
    idx = min(len(string), len(curSum))
    if curSum == string[:idx]:
        return helper(second, curSum, string[idx:])
    
    return False

def addString(first, second):
    return str(int(first) + int(second))

def valid(string):
    return string and len(string) == len(str(int(string)))
    

