from homework2.task3 import combinations


def test_combinations():
    assert combinations([1, 3], [4, 5]) == [(1, 4), (1, 5), (3, 4), (3, 5)]
