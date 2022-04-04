# O(N) Time | O(1) Space

# find the node before left and after right, reverse in between and connect it again
def reverseBetween(head, left, right):
    prevStart, nextEnd = getFrontAndBack(head, left, right)
    reversedHead = reverse(prevStart.next if prevStart else head)
    if prevStart:
        prevStart.next = reversedHead
    else:
        head = reversedHead
    connectEnds(head, nextEnd)
    return head
    
def getFrontAndBack(head, left, right):
    prevStart, nextEnd = None, None
    previous = None
    for i in range(1, right + 1):
        if i == left:
            prevStart = previous
        if i == right:
            nextEnd = head.next
            break
        previous = head
        head = head.next
    head.next = None 
    return prevStart, nextEnd

def connectEnds(node, nextEnd):
    while node.next:
        node = node.next
    node.next = nextEnd

def reverse(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next    
    return prev