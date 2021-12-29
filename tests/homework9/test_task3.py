import tempfile
from pathlib import Path

import pytest

from homework9.task3 import universal_file_counter


@pytest.fixture()
def temp_dir():
    with tempfile.TemporaryDirectory() as directory:
        yield Path(str(directory))


def test_universal_file_counter_without_tokenizer(temp_dir):
    with open(temp_dir / "file1.txt", "w") as fp:
        fp.write("1 \n2")
        fp.seek(0)
    with open(temp_dir / "file2.txt", "w") as fp:
        fp.write("1 2\n 4")
        fp.seek(0)
    assert universal_file_counter(temp_dir, "txt") == 4


def test_universal_file_counter_with_tokenizer(temp_dir):
    with open(temp_dir / "file1.txt", "w") as fp:
        fp.write("1 \n2")
        fp.seek(0)
    with open(temp_dir / "file2.txt", "w") as fp:
        fp.write("1 2\n 4")
        fp.seek(0)
    assert universal_file_counter(temp_dir, "txt", str.split) == 5
