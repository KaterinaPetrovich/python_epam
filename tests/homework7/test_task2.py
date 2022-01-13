from homework7.task2 import backspace_compare


def test_true_backspace_compare():
    assert backspace_compare("asd######aa", "#####as###aa")


def test_false_backspace_compare():
    assert not backspace_compare("as##aa", "as#aa")
