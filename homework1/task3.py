from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        array = [int(line.rstrip()) for line in fi]
    array.sort()
    return array[0], array[-1]
