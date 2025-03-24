class LRUCache:

    def __init__(self, capacity: int): # O(1), O(Capacity)
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int: # O(1), O(1)
        if key in self.cache:
            self.cache.move_to_end(key) # mark key as recently used
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None: # O(1), O(Capacity)
        if key in self.cache:
            self.cache.move_to_end(key) # mark key as recently used
        self.cache[key] = value # insert/update

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False) # evict the least recently used key


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
