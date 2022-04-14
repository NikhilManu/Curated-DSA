# Time O(N) | Space O(N)

def calculator(s):
    num, stack, prevSign = 0, [], '+'
    for i, val in enumerate(s):
        if val.isdigit():
            num = num * 10 + int(val)
        if val in '+-*/' or i == len(s) - 1:
            if prevSign == '+':
                stack.append(num)
            elif prevSign == '-':
                stack.append(-num)
            elif prevSign == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            num, prevSign = 0, val # reset 

    return sum(stack)

# Time O(N) | Space O(1)
# Instead of summing the stack at last just add the number with a variable

def calculator(s):
    num, sign = 0, '+'
    result, lastNumber = 0, 0
    for i, val in enumerate(s):
        if val.isdigit():
            num = num * 10 + int(val)
        if val in '+-*/' or i == len(s) - 1:
            if sign == '+':
                result += lastNumber
                lastNumber = num
            elif sign == '-':
                result += lastNumber
                lastNumber = -num
            elif sign == '*':
                lastNumber *= num
            else:
                lastNumber = int(lastNumber / num)
            num, sign = 0, val # reset 

    return result + lastNumber