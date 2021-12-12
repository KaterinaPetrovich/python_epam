def backspace_compare(first: str, second: str) -> bool:
    return make_list(first) == make_list(second)


def make_list(string: str) -> list[str]:
    char_list = []
    counter = 0
    string = "".join(reversed(string))
    for val in string:
        if val == "#":
            counter += 1
        elif counter != 0:
            counter -= 1
        else:
            char_list.append(val)
    return char_list
