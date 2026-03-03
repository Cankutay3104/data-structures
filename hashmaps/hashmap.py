class MyHashMap:
    """
    A basic Hash Map implementation using separate chaining for collision resolution.
    """
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index][i][1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                return self.table[index][i][1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if self.table[index][i][0] == key:
                self.table[index].remove(pair)
                return True
        return False