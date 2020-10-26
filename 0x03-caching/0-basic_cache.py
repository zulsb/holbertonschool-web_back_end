#!/usr/bin/python3
""" Module that creates a basic dictionary.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system.
        Overwrite functions 'put' and 'get'.
    """

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item
            value for the key.
        """
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return:
                The value in self.cache_data linked to key.
        """
        return self.cache_data.get(key)
