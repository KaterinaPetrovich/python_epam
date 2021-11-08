from .task2 import check_fibonacci, generate_fib


def test_positive_check_fibonacci():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21])


def test_negative_check_fibonacci():
    assert not check_fibonacci([0, 1, 2, 3, 5, 8, 6, 3])


def test_generate_fib():
    assert generate_fib(5) == [0, 1, 1, 2, 3]
