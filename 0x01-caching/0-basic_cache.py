#!/usr/bin/env python3
"""A module to implement basic caching"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Implements BasicCache class"""

    def __init__(self):
        """Initilizes the BasicCache class instances"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """Get an item with a specified key"""
        if key is None:
            return None
        return self.cache_data.get(key, None)