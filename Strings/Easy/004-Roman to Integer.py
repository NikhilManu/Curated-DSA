# Time O(N) | Space O(1)

def romanToInt(string):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    integer = 0
    for i in range(len(string) - 1):
        if roman[string[i]] < roman[string[i + 1]]:
            integer -= roman[string[i]]
        else:
            integer += roman[string[i]]

    return integer + roman[string[-1]] # Since we are not adding the last number, we adding it after the loop