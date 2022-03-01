import random

# Time O(1) | Space O(N)
class RandomizedSet:
    def __init__(self):
        self.lookup = {}
        self.nums = []
        
    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False
        
        self.lookup[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False
        
        idxOfVal, lastElement = self.lookup[val], self.nums[-1]
        self.nums[idxOfVal] = lastElement # modify current index with last Element.
        self.lookup[lastElement] = idxOfVal # Update Last Element's index with the new Index.
        self.lookup.pop(val) # Remove the val from the lookup.
        self.nums.pop() 
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.nums)


"""
    Here The only Problem is to remove a value from the list in Constant Time. 
    Since the order of the list doesnt matter. Just swap the current Element with last element and pop the last element.
"""
