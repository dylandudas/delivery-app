
# Custom Hash Table with iterator and length definitions
# along with hash, insert, and get methods
class HashTable:
    def __init__(self, buckets = 10):
        self.buckets = buckets
        self.table = [[] for _ in range(self.buckets)]
        self.length = 0

    def __iter__(self):
        for row in self.table:
            yield from row

    def hash(self, key):
        return int(key) % self.buckets

    def insert(self, key, value):
        index = self.hash(key)
        bucket = self.table[index]

        for item in bucket:
            if item[0] == key:
                return

        bucket.append([key, value])
        self.length += 1

    def get(self, key):
        index = self.hash(key)
        bucket = self.table[index]

        for item in bucket:
            if item[0] == key:
                return item[1]

        return None

    def __len__(self):
        return self.length

