from typing import Callable


def cache(func: Callable) -> Callable:
    memo = {}

    def wrapper(*args):
        try:
            return memo[args]
        except KeyError:
            memo[args] = func(*args)
            return memo[args]

    return wrapper
