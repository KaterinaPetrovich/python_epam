"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def backspace_compare(first: str, second: str) -> bool:
    return make_list(first) == make_list(second)




def make_list(string):
    char_list = []
    counter = 0
    string = ''.join(reversed(string))
    for val in string:
        if val == "#":
            counter += 1
        elif counter != 0:
            counter -= 1
        else:
            char_list.append(val)
    return char_list


s = "a#c"
t = "b"
print(backspace_compare(s,t))
