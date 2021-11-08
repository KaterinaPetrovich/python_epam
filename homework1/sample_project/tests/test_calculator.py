import pytest

from calculator.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(4)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(6)


def test_null():
    assert check_power_of_2(0) == 0
