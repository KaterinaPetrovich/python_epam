from collections.abc import Iterable
from typing import List


def custom_range(inp, stop_value, start=0, step=1) -> List:
    if not (isinstance(inp, Iterable) or
            all(isinstance(item, type(inp[0])) for item in inp)):
        raise ValueError("Invalid input")
    stop = inp.index(stop_value)
    if start != 0:
        start = inp.index(start)
    range_list = [inp[i] for i in range(start, stop, step)]
    return range_list
