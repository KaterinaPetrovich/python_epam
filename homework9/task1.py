from typing import Iterator, List


def merge_sorted_files(file_list: List[str]) -> Iterator:
    yield from sorted(generate_numbers_from_files(file_list))


def generate_numbers_from_files(file_list):
    for file in file_list:
        with open(file) as fp:
            for line in fp:
                yield int(line.rstrip())
