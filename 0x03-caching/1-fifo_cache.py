#!/usr/bin/python3
""" Module that creates a FIFO caching.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system.
        Overwrite functions 'put' and 'get' for implement FIFO caching system.
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
            self.cache_data[key] = item
            self.cache.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keyD = self.cache.pop(0)
            self.cache_data.pop(keyD)
            print("DISCARD: {}".format(keyD))

    def get(self, key):
        """ Return:
                The value in self.cache_data linked to key.
        """
        return self.cache_data.get(key)
