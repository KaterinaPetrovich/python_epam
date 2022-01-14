import tempfile

from homework9.task1 import merge_sorted_files


def test_merge_sorted_files():
    with tempfile.NamedTemporaryFile(mode="w+t") as fp:
        with tempfile.NamedTemporaryFile(mode="w+t") as ft:
            fp.write("1\n4\n")
            fp.seek(0)
            ft.write("2\n5\n")
            ft.seek(0)
            assert list(merge_sorted_files([fp.name, ft.name])) == [1, 2, 4, 5]
