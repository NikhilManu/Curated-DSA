# Time O(N) | Space O(1)

def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k

"""
- Since, our first element is already present at index 0, we quickly run a for loop for the entire array to scan for 
  unique elements.
- If the current element and the next element are the same, then we just keep on going till we find a different element
- Once we find a different element, it is inserted at index 1, because, index 0 is taken by the first unique element.
- Once this is done, the same scanning is done to find out the next unique element and this element is to be inserted at index 2. 
  This process continues until we are done with unique elements.
"""