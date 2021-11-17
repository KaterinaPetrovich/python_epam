import itertools
from typing import Any, List, Tuple


def combinations(*args: List[Any]) -> List[Tuple]:
    return list(itertools.product(*args))
