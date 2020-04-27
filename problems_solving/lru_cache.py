"""Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity."""

import collections

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        try:
            # reinsert key to keep least-used-order
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        """ 
        1. Try to remove key - reinserting key
        2. If KeyError raises, check the capacity and pop least-used
        3. Add key to cache
        """
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1;       # returns 1
    cache.put(3, 3);    # evicts key 2
    cache.get(2);       # returns -1 (not found)
    cache.put(4, 4);    # evicts key 1
    cache.get(1);       # returns -1 (not found)
    assert cache.get(3) == 3;       # returns 3
    assert cache.get(4) == 4;       # returns 4