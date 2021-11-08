from homework1.task4 import check_sum_of_four


def test_check_sum_of_four():
    assert check_sum_of_four([1, 2], [1, -2], [0, 2], [-1, 0]) == 2
