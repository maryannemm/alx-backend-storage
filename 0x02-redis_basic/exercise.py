#!/usr/bin/env python3
"""
This module contains the Cache class for storing and retrieving data from Redis.
It also tracks method calls and stores history for methods.
"""

import redis
import uuid
import functools
from typing import Union, Callable

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    
    Args:
        method: The method to be decorated.
    
    Returns:
        The wrapped method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Increment the count each time the method is called.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of method calls (inputs and outputs).

    Args:
        method: The method to be decorated.

    Returns:
        The wrapped method with input and output tracking.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Store the input parameters and output in Redis lists.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper

def replay(method: Callable):
    """
    Display the history of calls to a particular function.

    Args:
        method: The method to display the history for.
    """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, outp in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')}) -> {outp.decode('utf-8')}")

class Cache:
    """
    Cache class that interacts with Redis to store and retrieve data.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client.
        Flush the database to ensure it's clean on startup.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data and count the number of calls to this method.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """
        Retrieve data from Redis and optionally convert it using fn.

        Args:
            key: The Redis key.
            fn: An optional callable for data conversion.

        Returns:
            The stored data, optionally converted by fn.
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieve a string value from Redis.

        Args:
            key: The Redis key.

        Returns:
            The stored data as a string.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer value from Redis.

        Args:
            key: The Redis key.

        Returns:
            The stored data as an integer.
        """
        return self.get(key, int)

