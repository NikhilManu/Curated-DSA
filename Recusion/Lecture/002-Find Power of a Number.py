# Time O(N) | Space O(N)
def power(x, n):
    if n == 0:
        return 1
    
    return x * power(x, n - 1)

'''
Improvement:

pow(x, n) = x * pow(x, n - 1)
        OR
pow(x, n) = pow(x, n // 2) * pow(x, n // 2)
'''
# Time O(log N) | Space O(log N)
def power(x, n):
    if n == 0:
        return 1

    temp = power(x, n // 2)
    return temp * temp if n % 2 == 0 else temp * temp * x
    
'''
when n is Odd:
    let n = 7
        pow(x, 7) --> pow(x, 3)

        So if we remultiply it 
            pow(x, 3) * pow(x, 3) * x == pow(x, 7)

'''


