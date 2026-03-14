# LeetCode '705. Design HashSet' Solution
class MyHashSet(object):

    def __init__(self):
        self.size = 100
        self.table = [ [] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key):
        index = self._hash(key)
        if not self.contains(key):
            self.table[index].append(key)
        return

    def remove(self, key):
        index = self._hash(key)
        if self.contains(key):
            self.table[index].remove(key)
        return
        

    def contains(self, key):
        index = self._hash(key)
        
        for i in range(len(self.table[index])):
            if self.table[index][i] == key:
                return True
        return False