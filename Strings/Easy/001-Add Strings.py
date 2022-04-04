# Time O(N) | Space O(1)

def addString(num1, num2):
    p1, p2 = len(num1) - 1, len(num2) - 1
    carry, res = 0, []
    while p1 >= 0 or p2 >= 0 or carry > 0:
        if p1 >= 0:
            carry += int(num1[p1])
            p1 -= 1
        
        if p2 >= 0:
            carry += int(num2[p2])
            p2 -= 1
            
        res.append(str(carry % 10))
        carry //= 10
        
    return ''.join(res[::-1])