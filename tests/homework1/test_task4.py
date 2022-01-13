from homework1.task4 import check_four


def test_check_four():
    assert check_four([1, 2], [1, -2], [0, 2], [-1, 0]) == 2
