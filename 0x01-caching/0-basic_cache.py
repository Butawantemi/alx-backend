#!/usr/bin/env python3
"""A module to implement basic caching"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Implements BasicCache class"""

    def __init__(self):
        """Initilizes the Basiccache class"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache"""

        # check if the key or item is None
        if key is None or item is None:
            return None

        # add item to the cache_data dictionary
        self.cache_data[key] = item

    def get(self, key):
        """Get an item with a specified key"""

        # check if key is None or doesn't exist in the cache
        if key is None:
            return None

        # return the item or None if key doesn't exist
        return self.cache_data.get(key, None)
