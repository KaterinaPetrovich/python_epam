from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    if check_win(board, "x"):
        return "x wins"
    elif check_win(board, "o"):
        return "o wins"
    elif check_unfinished(board):
        return "unfinished"
    else:
        return "draw"


def check_unfinished(board):
    counter = 0
    for n in range(3):
        for m in range(3):
            if board[n][m] == "-":
                counter += 1
    return counter > 1


def check_win(board, char):
    for n in range(3):
        if board[n][0] == board[n][1] == board[n][2] == char:
            return True
        if board[0][n] == board[1][n] == board[2][n] == char:
            return True
    if board[0][0] == board[1][1] == board[2][2] == char:
        return True
    if board[0][2] == board[1][1] == board[2][0] == char:
        return True
    else:
        return False
