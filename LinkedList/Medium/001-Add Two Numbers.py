# Time O(max(n, m)) | Space O(1)

# Initial Code
def addNumbers(l1, l2):
    dummy = ListNode(-1)
    cur, rem = dummy, 0
    while l1 and l2:
        sum = l1.val + l2.val + rem
        cur.next = ListNode(sum % 10)
        rem = sum // 10
        
        cur = cur.next
        l1 = l1.next
        l2 = l2.next
    
    while l1:
        sum = l1.val + rem
        cur.next = ListNode(sum % 10)
        rem = sum // 10
        
        cur = cur.next
        l1 = l1.next
        
    while l2:
        sum = l2.val + rem
        cur.next = ListNode(sum % 10)
        rem = sum  // 10
        
        cur = cur.next
        l2 = l2.next
    
    if rem > 0:
        cur.next = ListNode(rem)
        
    return dummy.next

# Refactored Code
def addNumbers(l1, l2):
    dummy = ListNode(-1)
    cur, rem = dummy, 0
    while l1 or l2:
        sum = rem
        if l1:
            sum += l1.val
            l1 = l1.next
        
        if l2:
            sum += l2.val
            l2 = l2.next
            
        cur.next = ListNode(sum % 10)
        rem = sum // 10
        cur = cur.next
    
    if rem > 0:
        cur.next = ListNode(rem)
        
    return dummy.next

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next