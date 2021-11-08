import os
import tempfile

import pytest

from homework1.task3 import find_maximum_and_minimum


@pytest.fixture()
def test_file() -> str:
    temp_dir = tempfile.gettempdir()
    temp_file = f"{temp_dir}/new_file.txt"
    with open(temp_file, "w") as f:
        f.write("1" + "\n" + "2" + "\n" + "3")
    yield temp_file
    os.remove(temp_file)


def test_find_maximum_and_minimum(test_file):
    assert find_maximum_and_minimum(test_file) == (1, 3)
