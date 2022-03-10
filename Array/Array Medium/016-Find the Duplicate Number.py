# Time O(N) | Space O(1)

# Same as finding the start of cycle in a linkedlist
def findDuplicate(nums):
    slow, fast = nums[0], nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
            