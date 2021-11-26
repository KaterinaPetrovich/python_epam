import tempfile

from homework4.task1 import read_magic_number


def test_read_magic_number():
    with tempfile.NamedTemporaryFile(mode='w+t') as temp:
        temp.write("2")
        temp.seek(0)
        assert read_magic_number(temp.name)
