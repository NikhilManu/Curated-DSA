# Time O(N) | Space O(1)

def validNumber(s):
    digit, decimal, e, symbol = False, False, False, False
    for char in s:
        if char in '0123456789':
            digit = True
        elif char in '+-':
            if digit or decimal or symbol:
                return False
            else:
                symbol = True
        elif char in 'Ee':
            if not digit or e: 
                return False
            else:   
                e = True
                digit, decimal, symbol = False, False, False
        elif char == '.':
            if decimal or e:
                return False
            else:
                decimal = True
        else:
            return False
            
    return digit