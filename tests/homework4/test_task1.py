import tempfile

import pytest

from homework4.task1 import read_magic_number


def test_positive_read_magic_number():
    with tempfile.NamedTemporaryFile(mode='w+t') as fp:
        fp.write("2")
        assert read_magic_number(fp.name)


def test_string_read_magic_number():
    with tempfile.NamedTemporaryFile(mode='w+t') as fp:
        fp.write("asdfg")
        with pytest.raises(ValueError):
            read_magic_number(fp.name)


def test_out_of_interval_read_magic_number():
    with tempfile.NamedTemporaryFile(mode='w+t') as fp:
        fp.write("14")
        assert not read_magic_number(fp.name)
