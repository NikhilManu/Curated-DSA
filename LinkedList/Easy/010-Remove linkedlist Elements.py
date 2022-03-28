# Time O(N) | Space O(1)

def removeElements(head, val):
    newHead = cur = ListNode(-1)
    cur.next = head
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
            
    return newHead.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next