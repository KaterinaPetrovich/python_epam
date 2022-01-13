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
