from homework8.task1 import KeyValueStorage

storage = KeyValueStorage("./homework8/task1.txt")


def test_getitem():
    assert storage["name"] == "kek"


def test_get_attribute():
    assert storage.name == "kek"


def test_get_integer():
    assert isinstance(storage.power, int)
