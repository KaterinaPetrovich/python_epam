import pytest


def test_str_startswith():
    assert "abc".startswith("a")


def test_str_out_of_range():
    with pytest.raises(IndexError):
        "qwe"[12]


@pytest.mark.parametrize("test_input", ["aaa", "AAA", "aAA"])
def test_str_capitalize(test_input):
    assert test_input.capitalize() == "Aaa"


def test_find_len_set():
    my_set = {1, 2, 4}
    assert len(my_set) == 3


def test_pop_method_with_empty_set():
    my_set = {}
    with pytest.raises(TypeError):
        my_set.pop()


@pytest.mark.parametrize("test_input", [{1}, {}, {22, 4, 5, 1, 9}])
def test_issubset(test_input):
    set_a = {1, 9, 22, 4, 5}
    assert test_input.issubset(set_a)
