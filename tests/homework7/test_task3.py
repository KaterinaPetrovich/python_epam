from homework7.task3 import tic_tac_toe_checker

unfinished_board = [["-", "o", "o"], ["-", "x", "o"], ["x", "o", "x"]]

draw_board = [["o", "x", "o"], ["-", "x", "o"], ["x", "o", "x"]]

x_wins_board = [["x", "x", "o"], ["-", "x", "o"], ["o", "o", "x"]]

o_wins_board = [["x", "x", "o"], ["-", "x", "x"], ["o", "o", "o"]]


def test_unfinished_tic_tac_toe_checker():
    assert tic_tac_toe_checker(unfinished_board) == "unfinished"


def test_x_wins_tic_tac_toe_checker():
    assert tic_tac_toe_checker(x_wins_board) == "x wins"


def test_o_wins_tic_tac_toe_checker():
    assert tic_tac_toe_checker(o_wins_board) == "o wins"


def test_draw_tic_tac_toe_checker():
    assert tic_tac_toe_checker(draw_board) == "draw"
