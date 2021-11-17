from homework2.task1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_get_longest_diverse_words():
    assert "unmißverständliche" in get_longest_diverse_words("data.txt")


def test_get_rarest_char():
    assert "’" in get_rarest_char("data.txt")


def test_count_punctuation_chars():
    assert count_punctuation_chars("data.txt") > 5400


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("data.txt") > 2900


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("data.txt") == ["ä"]
