# Time O(5^n) | Space O(5^n)

def findStrobogrammatic(n):
    return helper(n, n)

def helper(n, length):
    if length == 0:
        return ['']

    if length == 1:
        return ['0', '1', '8']

    answerTillNow = helper(n, length - 2)

    res = []
    for number in answerTillNow:
        if length != n:
            res.append("0" + number + "0") # Since we dont want to add 0 in the leftmost/rightmost side 

        res.append("1" + number + "1")
        res.append("6" + number + "9")
        res.append("8" + number + "8")
        res.append("9" + number + "6")
    
    return res    