from homework3.task1 import cache


@cache(times=2)
def function(a, b):
    return a + b


def test_cache():
    some = "asdfghjkl", "qwertyuiop"
    a = function(*some)
    b = function(*some)
    assert a is b


def test_out_of_max_times_cache():
    some = "asdfghjkl", "qwertyuiop"
    a = function(*some)
    function(*some)
    c = function(*some)
    assert a is not c
