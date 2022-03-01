# O(N) Time | Space O(1)

def PlusOne(digits):
    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            
    return [1] + digits