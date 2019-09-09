from gameboard import *
from player import *
from computer_ai import *


def explain_input():
    print("""
    The game board is labeled with row numbers along the right and column numbers along the bottom.
    Once you've decided where to place your next piece, enter the row number followed by the column number, with a space in between.
    For example, if you wanted to place a piece in the bottom left square, you would enter "3 1" (3 for the row and 1 for the column)
    """)


def explain_rules():
    explain_board = Board(3, 3)
    explain_board.make_move('X', 0, 2)
    explain_board.make_move('X', 1, 2)
    explain_board.make_move('X', 1, 1)
    explain_board.make_move('X', 2, 0)
    explain_board.make_move('O', 0, 1)
    explain_board.make_move('O', 2, 2)
    explain_board.make_move('O', 1, 0)
    print("""
    In Tic Tac Toe, there are 2 players: one using 'X's and one using 'O's.
    Starting with the player using 'X's, you and the computer take turns placing a single piece on the board at a time.
    Neither player may place a piece in a space that is already taken.
    If either player manages to get 3 of their pieces on the board 'in a row', they win the game!
    3 pieces are considered to form a row if they form a horizontal line in a single row, a vertical line in a single column,
    or a diagonal line from a corner, accross the middle, and to the opposite corner.
    The board below shows an example of the 'X' player winning with a diagonal.
    """)
    print(explain_board)
    print('\tIf all 9 spaces on the board are filled without either player winning, the game results in a tie.')


def play_tictac():
    name = input('Hello, what\'s your name? ')
    print(f'\nWelcome, {name}. Let\'s play some tic tac toe!')
    rule_check = input(
        'Would you like me to explain the rules?\nPlease enter y/n: ').lower()
    while rule_check not in ['y', 'n']:
        print('\nSorry, that wasn\'t a valid input. Please enter \'y\' or \'n\'.')
        rule_check = input('Would you like me to explain the rules? ').lower()
    if rule_check:
        explain_rules()
    marker = input(
        '\nWould you like to be \'X\'s or \'O\'s?\nEnter x/o: ').upper()
    while marker not in ['X', 'O']:
        print('\nSorry, that wasn\'t a valid input. Please enter \'x\' or \'x\'.')
        marker = input('Would you like to be \'X\'s or \'O\'s? ').upper()
    new_player = Player(name, marker)
    # if new_player.marker == 'X':
    #     new_robot = 'O'  # FIX THIS
    # if new_player.marker == 'O':
    #     new_robot = 'X'  # FIX THIS
    tictac = Board(3, 3)
    inputting_check = input(
        'Would you like me to explain how to input your moves?\nPlease enter y/n: ').lower()
    while inputting_check not in ['y', 'n']:
        print('\nSorry, that wasn\'t a valid input. Please enter \'y\' or \'n\'.')
        inputting_check = input(
            'Would you like me to explain how to input your moves? ').lower()
    if inputting_check:
        print('\n')
        print(tictac)
        explain_input()
    input('Let\'s get started! Press enter when you\'re ready.')

    # Start the game
    while not tictac.check_game_end():
        print('\n')
        print(tictac)
        row, column = new_player.prompt_move(tictac)
        tictac.make_move(new_player.marker, row, column)


play_tictac()

# tictac = Board(3, 3)
# tictac.make_move(new_player.marker, 2, 2)
# tictac.make_move(new_player.marker, 1, 2)


# comp1_marker = 'X'
# comp2_marker = 'O'
# tictac.make_move(comp1_marker, 0, 0)
# tictac.make_move(comp2_marker, 0, 1)
# x, y = decide_next_move(tictac, comp1_marker, comp2_marker)
# tictac.make_move(comp1_marker, x, y)
# x, y = decide_next_move(tictac, comp2_marker, comp1_marker)
# tictac.make_move(comp2_marker, x, y)
# x, y = decide_next_move(tictac, comp1_marker, comp2_marker)
# tictac.make_move(comp1_marker, x, y)
# x, y = decide_next_move(tictac, comp2_marker, comp1_marker)
# tictac.make_move(comp2_marker, x, y)
# x, y = decide_next_move(tictac, comp1_marker, comp2_marker)
# tictac.make_move(comp1_marker, x, y)

# print(tictac)
