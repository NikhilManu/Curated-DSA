# Time O(N) | Space O(N)

def calculator(s):
    num, stack, sign = 0, [], '+'
    for i, val in enumerate(s):
        if val.isdigit():
            num = num * 10 + int(val)
        if val in '+-*/' or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            num, sign = 0, val # reset 
            
    return sum(stack)