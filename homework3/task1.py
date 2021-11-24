from collections import defaultdict


def cache(times):
    def wrapper(func):
        memo = {}
        counter = defaultdict(int)

        def inner(*args, **kwargs):
            counter[args] += 1
            if counter[args] > times:
                del memo[args]
            try:
                return memo[args]
            except KeyError:
                memo[args] = func(*args, **kwargs)
                return memo[args]

        return inner
    return wrapper
