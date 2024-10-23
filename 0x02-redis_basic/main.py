#!/usr/bin/env python3
"""
Main file for testing the Cache class and its features.
"""

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

# Test storing and retrieving data
data = b"hello"
key = cache.store(data)
print(key)

# Test retrieving data
print(cache.get(key))
print(cache.get_str(key))

# Test storing call history
s1 = cache.store("first")
s2 = cache.store("second")
s3 = cache.store("third")

# Display the call history
inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

print("inputs:", inputs)
print("outputs:", outputs)

# Test replay functionality
replay(cache.store)

