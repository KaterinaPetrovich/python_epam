from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) == 0:
        return False
    fib = generate_fib(len(data))
    return fib == data


def generate_fib(n: int) -> Sequence[int]:
    if n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib
