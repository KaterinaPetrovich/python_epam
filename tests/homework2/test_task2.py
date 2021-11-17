from homework2.task2 import major_and_minor_elem


def test_major_and_minor_elem():
    assert major_and_minor_elem([1, 1, 1, 2, 2, 3, 1]) == (1, 3)
