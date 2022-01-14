from homework9.task2 import Suppressor, suppress_exception


def test_suppress_exception():
    with suppress_exception(ZeroDivisionError):
        result = 1 / 0
        assert bool(result)


def test_class_suppressor():
    with Suppressor(ZeroDivisionError):
        result = 1 / 0
        assert bool(result)
