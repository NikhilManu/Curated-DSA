"""
 Before starting this question you should know
    => hashing functions and what they do
    => what are collisions --> Resolving Techniques are Chaining, Open Addressing
    => load factor

Another Improvement we can come with is to implement some Red Black Tree (Self balancing Binary Tree) inside each buckets.
But the important concept here is chaining and how the hashSet works
"""
# Basic HashSet with Chaining as Collision resolving Technique
class MyHashSet:
    def __init__(self):
        self.size = 15000
        self.buckets = [None] * self.size
    
    def hash(self, key):
        return key % self.size
    
    def add(self, key: int) -> None:
        i = self.hash(key)
        if not self.buckets[i]:
            self.buckets[i] = []
        if key not in self.buckets[i]:
            self.buckets[i].append(key)

    def remove(self, key: int) -> None:
        i = self.hash(key)
        if self.buckets[i] and key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self, key: int) -> bool:
        i = self.hash(key)
        return self.buckets[i] and key in self.buckets[i]


# Resizable HashSet with Chaining
class MyHashSet:
    def __init__(self):
        self.size = 16
        self.loadFactor = 0.75 # Making LF = 75%, so when 75% keys are filled we resize the buckets
        self.buckets = [None] * self.size
        self.count = 0
    
    def hash(self, key):
        return key % self.size
    
    def reHash(self):
        self.size *= 2
        newBucket = [None] * self.size
        for bucket in self.buckets:
            if not bucket:
                continue
            for key in bucket:
                hashValue = self.hash(key)
                if not newBucket[hashValue]:
                    newBucket[hashValue] = []
                newBucket[hashValue].append(key)
                
        self.buckets = newBucket
        
    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        if self.loadFactor * self.size == self.count:
            self.reHash()
            
        i = self.hash(key)
        if not self.buckets[i]:
            self.buckets[i] = []
        self.buckets[i].append(key)
        self.count += 1

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        
        i = self.hash(key)
        self.buckets[i].remove(key)
        self.count -= 1

    def contains(self, key: int) -> bool:
        i = self.hash(key)
        return self.buckets[i] and key in self.buckets[i]
    
