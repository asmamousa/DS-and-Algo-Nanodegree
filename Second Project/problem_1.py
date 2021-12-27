from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity < 0:
            raise Exception("Cache can't have negative capacity")
        if capacity == 0:
            raise Exception("Cache can't have zero-value capacity")
        self.cache_size = capacity
        self.LRU_dict = OrderedDict()

    def get(self, key):
        # Retrieve from cache if exist and move that (key,value) pair to the end of dict as it was hitted
        # and if the key is not exist return -1
        if key is None:
            return

        if key in self.LRU_dict:
            self.LRU_dict.move_to_end(key)
            return self.LRU_dict[key]
        else:
            return -1

    def set(self, key, value):
        # Set the key,value pair in the dict if it's not exist
        # while if it exist remove the front(LRU) of the dict and add the pair after that
        if key is None or value is None:
            return

        if key not in self.LRU_dict:
            if len(self.LRU_dict) >= self.cache_size:
                self.LRU_dict.popitem(last=False)

            self.LRU_dict[key] = value
        else:
            return -1


# test case 0: add non-existed items
LRU_cache = LRU_Cache(6)
LRU_cache.set('a', 1)
LRU_cache.set('m', 5)
LRU_cache.set('e', 3)
LRU_cache.set('c', 9)

# test case 1: retrieve existed items
print (LRU_cache.get('a'))
# returns 1
print (LRU_cache.get('e'))  
# returns 3

# test case 2: retrieve non-existed items
print (LRU_cache.get('ss'))
# returns -1 because 'ss' is not present in the cache

# test case 3: add non-existed items to fill up the cache then add item with key 'F'
LRU_cache.set('r', 88)
LRU_cache.set('x', 7)
LRU_cache.set('F', 12)
print (LRU_cache.get('m'))
# returns -1 because the cache reached it's capacity and m was the least recently used entry

# test case 4: add existed item to cache
print (LRU_cache.set('r', 100))
# returns -1 because the 'r' key is alreay in the cache

# test case 5: try calling get() with None key
print (LRU_cache.get(None))
# returns None

# test case 6: try calling set() with None key or None Value
print (LRU_cache.set(None, 6))
print (LRU_cache.set('t', None))
print (LRU_cache.set(None, None))
# returns None


# test case 7: capacity is negative value or 0
LRU_cache2 = LRU_Cache(-2)
LRU_cache2.set('E', 100)
# returns an exception with the message "Cache can't have negative capacity"

LRU_cache2 = LRU_Cache(0)
LRU_cache2.set('E', 100)
# returns an exception with the message "Cache can't have zero-value capacity"