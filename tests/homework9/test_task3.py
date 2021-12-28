import tempfile

from homework9.task3 import universal_file_counter


def test_universal_file_counter_without_tokenizer():
    with tempfile.NamedTemporaryFile(
            mode="w+t", dir="./homework9", suffix="txt"
    ) as fp:
        with tempfile.NamedTemporaryFile(
            mode="w+t", dir="./homework9", suffix="txt"
        ) as ft:
            fp.write("1 s s\n4")
            fp.seek(0)
            ft.write("2\n5")
            ft.seek(0)
            assert universal_file_counter("./homework9", "txt") == 4


def test_universal_file_counter_with_tokenizer():
    with tempfile.NamedTemporaryFile(
            mode="w+t", dir="./homework9", suffix="txt"
    ) as fp:
        with tempfile.NamedTemporaryFile(
            mode="w+t", dir="./homework9", suffix="txt"
        ) as ft:
            fp.write("1 s s\n4")
            fp.seek(0)
            ft.write("2\n5")
            ft.seek(0)
            assert universal_file_counter("./homework9", "txt", str.split) == 6
