# TIme O(N) | Space O(1)

def intToRoman(num):
    integer = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    
    res = []
    for k in integer:
        while num >= k:
            res.append(integer[k])
            num -= k
            
    return ''.join(res)