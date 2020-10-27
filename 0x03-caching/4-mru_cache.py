#!/usr/bin/python3
""" Module that creates a MRU caching.
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system.
        Overwrite functions 'put' and 'get' for implement MRU caching system.
    """

    def __init__(self):
        """ Initiliaze.
        """
        super().__init__()
        self.cache = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item
            value for the key.
        """
        if key and item is not None:
            if key not in self.cache_data:
                self.cache.append(key)
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keyD = self.cache.pop(-2)
            self.cache_data.pop(keyD)
            print("DISCARD: {}".format(keyD))

    def get(self, key):
        """ Return:
                The value in self.cache_data linked to key.
        """
        if key is not None and key in self.cache_data:
            self.cache.remove(key)
            self.cache.append(key)
        return self.cache_data.get(key)
