import pytest

from homework2.task5 import custom_range


def test_positive_custom_range():
    assert (custom_range("qwertyu", "q", "u", -2)) == ["u", "t", "e"]


def test_exeption():
    with pytest.raises(ValueError):
        custom_range((5, "d"), "q", "u", -2)
