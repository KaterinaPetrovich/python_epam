from homework3.task4 import is_armstrong


def test_positive_is_armstrong():
    assert is_armstrong(153)


def test_negative_is_armstrong():
    assert not is_armstrong(100)
