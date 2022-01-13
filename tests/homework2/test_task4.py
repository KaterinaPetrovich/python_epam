from homework2.task4 import cache


def test_cache():
    counter = 0

    def function(a, b):
        nonlocal counter
        counter += 1
        return a+b

    cache_func = cache(function)
    some = 100, 200
    cache_func(*some)
    cache_func(*some)
    cache_func(*some)
    assert counter == 1
