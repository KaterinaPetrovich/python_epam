import unicodedata
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode-escape") as file:
        longest_words = ["" for n in range(10)]
        for word in tokenize(file):
            for i, longest_word in enumerate(longest_words):
                if len(set(word)) > len(longest_word) and word not in longest_words:
                    longest_words[i] = word
    return ["".join(x) for x in longest_words]


def tokenize(file):
    buffer = []
    while char := file.read(1):
        if char.isalpha():
            buffer += char
            continue
        else:
            if buffer:
                yield buffer
            buffer = []


def get_rarest_char(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode-escape") as file:
        count_dict = {}
        while char := file.read(1):
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return [k for k, v in count_dict.items() if v == min(count_dict.values())]


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as file:
        counter = 0
        while char := file.read(1):
            if unicodedata.category(char)[0] == "P":
                counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as file:
        counter = 0
        while char := file.read(1):
            if not char.isascii():
                counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode-escape") as file:
        count_dict = {}
        while char := file.read(1):
            if not char.isascii():
                if char in count_dict:
                    count_dict[char] += 1
                else:
                    count_dict[char] = 1
    return [k for k, v in count_dict.items() if v == max(count_dict.values())]
