# Same Concept as HashSet

# Resizable HashMap with loadFactor as 75% (Collision Resolving Technique used--> Chaining)
class MyHashMap:
    
    def __init__(self):
        self.size = 16
        self.buckets = [None] * self.size
        self.loadFactor = 0.75
        self.count = 0
    
    def hash(self, key):
        return key % self.size
    
    def reHash(self):
        self.size *= 2
        newBucket = [None] * self.size
        for bucket in self.buckets:
            if not bucket:
                continue
            for key, value in bucket:
                index = self.hash(key)
                if not newBucket[index]:
                    newBucket[index] = []
                newBucket[index].append([key, value])    
        self.buckets = newBucket
    
    def put(self, key: int, value: int) -> None:
        idx = self.contains(key)
        index = self.hash(key)
        if idx == -1:
            if self.size * self.loadFactor == self.count:
                self.reHash()
                index = self.hash(key)
            if not self.buckets[index]:
                self.buckets[index] = []
            self.buckets[index].append([key, value])
            self.count += 1
        else:
            self.buckets[index][idx][1] = value
            
        
    def get(self, key: int) -> int:
        index = self.hash(key)
        idx = self.contains(key)
        return -1 if idx == -1 else self.buckets[index][idx][1]

    def remove(self, key: int) -> None:
        index = self.hash(key)
        idx = self.contains(key)
        if idx == -1: return 
        self.buckets[index] = self.buckets[index][:idx] + self.buckets[index][idx + 1:]  
        self.count -= 1
        
    def contains(self, key):
        idx = self.hash(key)
        if not self.buckets[idx]:
            return -1
        
        for index, [k, v] in enumerate(self.buckets[idx]):
            if key == k:
                return index
        return -1
