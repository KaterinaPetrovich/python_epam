def is_armstrong(number: int) -> bool:
    st = str(number)
    return sum(list(map(lambda x: int(x) ** len(st), st))) == number
