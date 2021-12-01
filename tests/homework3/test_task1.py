from homework3.task1 import cache


def test_out_of_max_times_cache():
    counter = 0

    @cache(times=2)
    def function(a, b):
        nonlocal counter
        counter += 1
        return a+b

    some = 100, 200
    function(*some)
    function(*some)
    function(*some)
    assert counter == 2
