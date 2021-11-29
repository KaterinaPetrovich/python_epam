from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    """
    result = []
    for number in range(1, n+1):
        if number % 15 == 0:
            result.append("fizzbuzz")
        elif number % 3 == 0:
            result.append("fizz")
        elif number % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(number))
    return result
