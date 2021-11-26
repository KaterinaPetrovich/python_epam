def read_magic_number(path: str) -> bool:
    try:
        with open(path) as file:
            number = float(file.readline(1))
    except Exception:
        raise ValueError("Invalid input")
    return 1 <= number < 3
