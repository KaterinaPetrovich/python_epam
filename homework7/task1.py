from typing import Any
from collections import abc


def find_occurrences(obj: dict, element: Any, counter) -> int:
    if isinstance(obj, abc.Mapping):
        counter += find_occurrences(obj.keys(), element, 0)
        counter += find_occurrences(obj.values(), element, 0)

    elif isinstance(obj, abc.Collection) and not isinstance(obj, str):
        for item in obj:
            counter += find_occurrences(item, element, 0)
    else:
        return int(obj == element)

    return counter
