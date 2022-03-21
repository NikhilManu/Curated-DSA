# Time O(N) | Space O(N)

import random
class RandomizedCollection:
    
    def __init__(self):
        self.dic = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.dic[val] = set()
        self.dic[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.dic[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.dic or len(self.dic[val]) == 0:
            return False
        
        lastElement = self.nums[-1]
        idxToRemove = self.dic[val].pop()
        
        self.nums[idxToRemove] = lastElement
        self.dic[lastElement].add(idxToRemove)
        
        self.nums.pop()
        self.dic[lastElement].remove(len(self.nums))
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)    


"""
Logic is almost similar to that of the Meidum question. Only difference is that we are storing index of each value inside a set
"""