from homework5.task2 import custom_sum


def test_custom_sum_name():
    assert custom_sum.__name__ == "custom_sum"


def test_custom_sum_doc():
    expected = "This function can sum any objects which have __add___"
    assert custom_sum.__doc__ == expected


def test_custom_sum_attr_original_func():
    assert custom_sum.__original_func(1, 3) == 4
