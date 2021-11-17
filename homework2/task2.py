from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    cnt = Counter(inp)
    major_elem = cnt.most_common()[0][0]
    minor_elem = cnt.most_common()[-1][0]
    return major_elem, minor_elem
