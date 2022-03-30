# Time O(N) | Space O(1)

def copyList(head):
    if not head: return
    
    cur = head
    while cur:
        next = cur.next
        cur.next = Node(cur.val, next)
        cur = next
        
    cur = head
    while cur:
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next
        
    cur = head
    node = copy = head.next
    while cur:
        cur.next = cur.next.next
        node.next = node.next.next if node.next else None
        cur = cur.next
        node = node.next
        
    return copy

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""
    1 --> 2 --> 3 --> 4 --> None

    1 --> 1 --> 2 --> 2 --> 3 --> 3 --> 4 --> 4 --> None
    This is the intution, now we can connect random pointer easily
"""