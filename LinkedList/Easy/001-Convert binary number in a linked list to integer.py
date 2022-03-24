# TIme O(N) | Space O(1)

# First Intution - Reverse and calculate
def getDecimal(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
        
    i, decimal = 0, 0
    while prev:
        decimal += prev.val * (2 ** i)
        i += 1
        prev = prev.next
        
    return decimal

# TIme O(N) | Space O(1)

def getDecimal(head):
    sum = 0
    while head:
        sum *= 2
        sum += head.val
        head = head.next

    return sum

"""
So lets try converting decimal 123 => decimal 123 itself

Loop	Character	Operation	  Result
1	     1	        1	          1
2	     2	        (1x10) + 2	  12
3	     3 	        (12*10) + 3	  123

Above operation is always multiplied by the counting system, so for out case it will 2

Let convert (1101) => 13
Loop	Character	Operation	  Result
1	     1	        (0*1) + 1	  1
2	     1 	        (1x2) + 1	  3
3	     0	        (3*2) + 0	  6
4	     1 	        (6*2) + 1	  13

"""