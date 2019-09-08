from math import inf
from copy import deepcopy


def max_value(board):
    if not board.available_spaces:
        return 0
    value = -inf
    for row, column in board.available_spaces:
        temp_board = deepcopy(board)
        temp_board.make_move('X', row, column)
        print(f'MAX PRINT\n{temp_board}')
        if check_win(temp_board, 'X'):
            print('MAX PRINT - win')
            return inf
        value = max(value, min_value(temp_board))
    print('MAX PRINT', value)
    return value


def min_value(board):
    if not board.available_spaces:
        return 0
    value = inf
    for row, column in board.available_spaces:
        temp_board = deepcopy(board)
        temp_board.make_move('O', row, column)
        print(f'MIN PRINT\n{temp_board}')
        if check_win(temp_board, 'O'):
            print('MIN PRINT - win')
            return -inf
        value = min(value, max_value(temp_board))
    print('MIN PRINT', value)
    return value


def check_win(board, marker):
    winning_rows = [[(0, 0), (0, 1), (0, 2)], [
        (1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]
    winning_columns = [[(0, 0), (1, 0), (2, 0)], [
        (0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
    winning_diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    for row in winning_rows:
        win = True
        for x, y in row:
            if board[x][y] != marker:
                win = False
        if win:
            return True
    for col in winning_columns:
        win = True
        for x, y in col:
            if board[x][y] != marker:
                win = False
        if win:
            return True
    for diag in winning_diagonals:
        win = True
        for x, y in diag:
            if board[x][y] != marker:
                win = False
        if win:
            return True
    return False
