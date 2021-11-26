def read_magic_number(path: str) -> bool:
    try:
        with open(path) as file:
            number = float(file.readline(1))
    except ValueError as val_err:
        raise val_err
    return 1 <= number < 3
