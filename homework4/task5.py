from itertools import zip_longest


def fizzbuzz(n: int):
    """
    >>> fizzbuzz(6)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz']
    """
    numbers = [str(num) for num in range(n + 1)]
    fizz_index = list(fizz_sequence(n))
    buzz_index = list(buzz_sequence(n))
    fizzbuzz_index = list(fizzbuzz_sequence(n))
    for i in fizz_index:
        numbers[i] = "fizz"
    for i in buzz_index:
        numbers[i] = "buzz"
    for i in fizzbuzz_index:
        numbers[i] = "fizzbuzz"
    del numbers[0]
    return numbers


def fizz_sequence(n: int):
    num = 0
    while num < n + 1:
        yield num
        num += 3


def buzz_sequence(n: int):
    num = 0
    while num < n + 1:
        yield num
        num += 5


def fizzbuzz_sequence(n: int):
    num = 0
    while num < n + 1:
        yield num
        num += 15
