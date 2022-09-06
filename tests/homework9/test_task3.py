import os.path
import tempfile

from homework9.task3 import universal_file_counter


def test_universal_file_counter_without_tokenizer():
    with tempfile.TemporaryDirectory() as directory:
        temp_dir = os.path.abspath(directory)
        with open(temp_dir / "file1.txt", "w") as fp:
            fp.write("1 \n2")
            fp.seek(0)
        with open(temp_dir / "file2.txt", "w") as fp:
            fp.write("1 2\n 4")
            fp.seek(0)
        assert universal_file_counter(temp_dir, "txt") == 4


def test_universal_file_counter_with_tokenizer():
    with tempfile.TemporaryDirectory() as directory:
        temp_dir = os.path.abspath(directory)
        with open(temp_dir / "file1.txt", "w") as fp:
            fp.write("1 \n2")
            fp.seek(0)
        with open(temp_dir / "file2.txt", "w") as fp:
            fp.write("1 2\n 4")
            fp.seek(0)
        assert universal_file_counter(temp_dir, "txt", str.split) == 5
