# Time O(N) | Space O(1)

def mergeList(list1, list2):
    head = ListNode(-1)
    cur = head
    
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
            
        cur = cur.next
        
    cur.next = list1 or list2
    return head.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next