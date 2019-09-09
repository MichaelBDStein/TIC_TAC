from math import inf
from copy import deepcopy


# Minimax functions with alpha-beta optimizing. No heuristics, so only three possible values: inf (win), -inf (lose), and tie (0).
# These also take the markers ('X' or 'O') as arguments so that it can be run from either X's or O's perspective as the max value.
# Further, any symbol could be used on the game board, instead of 'X' or 'O'.
def max_value(board, good_marker, bad_marker, alpha=-inf, beta=inf):
    if not board.available_spaces:
        return 0
    value = alpha
    for row, column in board.available_spaces:
        temp_board = deepcopy(board)
        temp_board.make_move(good_marker, row, column)
        if temp_board.check_win(good_marker):
            return inf
        value = max(value, min_value(
            temp_board, good_marker, bad_marker, alpha, beta))
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return value


def min_value(board, good_marker, bad_marker, alpha=-inf, beta=inf):
    if not board.available_spaces:
        return 0
    value = beta
    for row, column in board.available_spaces:
        temp_board = deepcopy(board)
        temp_board.make_move(bad_marker, row, column)
        if temp_board.check_win(bad_marker):
            return -inf
        value = min(value, max_value(
            temp_board, good_marker, bad_marker, alpha, beta))
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value


# Minimax will only be called from this next function. This may be somewhat redundant.
# However, we need a board position for the next move to be returned, not just the value of the line of play.
# Since we don't care about the board positions for plays on deeper plys during the minimax recursion,
# and since it would hurt readability to have row and column variables being thrown back up the stack in the recursive call,
# I decided to separate the root node of the game tree, making it a simple iteration that saves the row and column associated with the highest value play.
def decide_next_move(board, good_marker, bad_marker):
    best_option = [-inf, (None)]
    for row, column in board.available_spaces:
        considering = deepcopy(board)
        considering.make_move(good_marker, row, column)
        result = min_value(considering, good_marker, bad_marker)
        if result > best_option[0] or not best_option[1]:
            best_option = [result, (row, column)]
            if best_option[0] == inf:
                break
    return best_option[1]
