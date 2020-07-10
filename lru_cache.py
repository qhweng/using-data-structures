from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.table = OrderedDict()
        self.size = capacity
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.size < 1:
            return -1
        
        try:
            value = self.table.pop(key)
            self.table[key] = value
            return value
        except:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache, if the cache is at capacity remove the oldest item.
        if self.size < 1:
            return

        try:
            value = self.table.pop(key)
            self.table[key] = value
        except:
            if len(self.table) >= self.size:
                self.table.popitem(last=False)
            self.table[key] = value

    def printCache(self):
        print(self.table)
        
            
def test(): 
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    # Test regular cases
    assert our_cache.get(1) == 1    # returns 1
    assert our_cache.get(2) == 2    # returns 2
    assert our_cache.get(9) == -1   # returns -1 b/c 9 is not in the cache

    # Test inserting None value and getting the same key value
    our_cache.set(5, 5) 
    our_cache.set(6, None)

    assert our_cache.get(3) == -1   # returns -1 b/c cache reached it's capacity and 3 was the least recently used entry
    assert our_cache.get(6) == None # returns None since no value
    assert our_cache.get(5) == 5    # returns 5
    assert our_cache.get(5) == 5    # returns 5
    assert our_cache.get(5) == 5    # returns 5

    # Test empty cache with set and get
    empty_cache = LRU_Cache(0)
    empty_cache.set(1, 1);
    assert empty_cache.get(1) == -1 # returns -1, nothing should be in cache

test()
