from homework9.task3 import universal_file_counter


def test_universal_file_counter_without_tokenizer():
    assert universal_file_counter("./homework8/", "txt") == 4


def test_universal_file_counter_with_tokenizer():
    assert universal_file_counter("./homework8/", "txt", str.split) == 4
