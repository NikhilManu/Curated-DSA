# Time O(N) | Space O(1)

# Find length, add zeros to the short Linkedlist and add using recursion
def addTwoNumbers(l1, l2):
    len1, len2 = getLength(l1), getLength(l2)
    if len1 > len2:
        l2 = addLeadingZeros(l2, len1 - len2)
    else:
        l1 = addLeadingZeros(l1, len2 - len1)
        
    node, carry = getSum(l1, l2)
    if carry > 0:
        newNode = ListNode(carry)
        newNode.next = node
        node = newNode
        
    return node
    
def getSum(l1, l2):
    if not l1 and not l2:
        return None, 0
    
    node, carry = getSum(l1.next, l2.next)
    sum = l1.val + l2.val + carry
    newNode = ListNode(sum % 10)
    newNode.next = node
    return newNode, sum // 10
    
def addLeadingZeros(node, length):
    for _ in range(length):
        newNode = ListNode(0)
        newNode.next = node
        node = newNode
        
    return node
    
def getLength(node):
    length = 0
    while node:
        node = node.next
        length += 1
        
    return length

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next