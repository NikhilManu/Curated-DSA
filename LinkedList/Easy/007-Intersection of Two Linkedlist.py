# Time O(N) | Space O(1)

# TwoPass --> Get the length and cutshort the longer Linkedlist
def intersection(headA, headB):
    if not headA or not headB:
        return
    lenA, lenB = getLength(headA), getLength(headB)
    
    if lenA > lenB:
        headA = traverseExtra(headA, abs(lenA - lenB))
    else:
        headB = traverseExtra(headB, abs(lenA - lenB))
        
    while headA is not headB:
        headA = headA.next if headA else None
        headB = headB.next if headB else None
        
    return headA
        
def traverseExtra(node, distance):
    for _ in range(distance):
        node = node.next
    return node

def getLength(node):
    length = 0
    while node and node.next:
        node = node.next
        length += 1
        
    return length

# Time O(N) | Space O(1)

# Similar to linkedlist Cycle - I prefer the first method
def intersection(headA, headB):
    a, b = headA, headB
    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA
        
    return a