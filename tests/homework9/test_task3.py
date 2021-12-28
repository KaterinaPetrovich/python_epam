import tempfile
from pathlib import Path

import pytest

from homework9.task3 import universal_file_counter


@pytest.fixture()
def temp_dir():
    with tempfile.TemporaryDirectory() as directory:
        with open(temp_directory / "file1.txt", "w") as file:
            file.write("1 \n2")
        with open(temp_directory / "file2.txt", "w") as file:
            file.write("1 2\n 4")
        yield Path(str(directory))


def test_universal_file_counter_without_tokenizer(temp_dir):
    assert universal_file_counter(temp_dir, "txt") == 4


def test_universal_file_counter_with_tokenizer(temp_dir):
    assert universal_file_counter(temp_dir, "txt", str.split) == 5
