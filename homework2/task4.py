from typing import Callable


def cache(func: Callable) -> Callable:
    memo = {}

    def wrapper(*args, **kwargs):
        try:
            return memo[args]
        except KeyError:
            memo[args] = func(*args, **kwargs)
            return memo[args]

    return wrapper


def function():
    return input('? ')

cache_func = cache(function)
'''
cache_func()
print("g")
cache_func()
print("b")
cache_func()
'''

cache_func()
cache_func()