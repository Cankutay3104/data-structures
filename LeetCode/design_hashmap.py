# LeetCode "706. Design HashMap" Solution

class MyHashMap(object):

    def __init__(self):
        self.size = 100
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def _find_index(self, bucket, key):
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return i
        return -1

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        existing = self._find_index(bucket, key)
        if existing != -1:
            bucket[existing][1] = value
        else:
            bucket.append([key, value])
        
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        existing = self._find_index(bucket, key)
        return bucket[existing][1] if existing != -1 else -1

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        existing = self._find_index(bucket, key)
        if existing != -1:
            bucket.pop(existing)