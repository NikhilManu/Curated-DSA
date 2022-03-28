# Time O(N) | Space O(1)

# Find the middle, reverse any side and check if they are equal
def isPalindrome(head):
    if not head.next:
        return True
    
    mid = getMiddle(head)
    tail = reverse(mid)
    
    while head:
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.next
    return True
    
def reverse(node):
    prev = None
    while node:
        node.next, prev, node = prev, node, node.next
    return prev
    
def getMiddle(head):
    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    return slow