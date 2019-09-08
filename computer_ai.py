# def max_value(value, depth, alpha, beta):
#     if depth == 0 and value:
#         return value


# def min_value(value, depth, alpha, beta):
#     return


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


available_spaces = [(x, y) for x in range(3) for y in range(3)]
