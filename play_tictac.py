from gameboard import *
from player import *
from computer_ai import *


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
    Starting with the player using 'X's, you and our resident robot, 'Robey' will take turns placing a single piece on the board.
    Neither player may place a piece in a space that is already taken.
    If either player manages to get 3 of their pieces on the board 'in a row', they win the game!
    3 pieces are considered to be 'in a row' if they form a horizontal line in a single row, a vertical line in a single column,
    or a diagonal line from a corner, accross the middle, and to the opposite corner.
    The board below shows an example of the 'X' player winning with a diagonal.
    """)
    print(explain_board)
    print('\tIf all 9 spaces on the board are filled without either player winning, the game results in a tie.')


def explain_input():
    print("""
    The game board is labeled with row numbers along the right and column numbers along the bottom.
    Once you've decided where to place your next piece, enter the row number followed by the column number, with a space in between.
    For example, if you wanted to place a piece in the bottom left square, you would enter "3 1" (3 for the row and 1 for the column)
    """)


def play_tictac(name):
    marker = input(
        '\nWould you like to be \'X\'s or \'O\'s?\nEnter x/o: ').upper()
    while marker not in ['X', 'O']:
        print('\nSorry, that wasn\'t a valid input. Please enter \'x\' or \'x\'.')
        marker = input('Would you like to be \'X\'s or \'O\'s? ').upper()
    new_player = Player(name, marker)
    if new_player.marker == 'X':
        robey_marker = 'O'  # FIX THIS
    if new_player.marker == 'O':
        robey_marker = 'X'  # FIX THIS
    tictac = Board(3, 3)
    input_explanation_needed = input(
        '\nWould you like me to explain how to input your moves?\nPlease enter y/n: ').lower()
    while input_explanation_needed not in ['y', 'n']:
        print('\nSorry, that wasn\'t a valid input. Please enter \'y\' or \'n\'.')
        input_explanation_needed = input(
            'Would you like me to explain how to input your moves? ').lower()
    if input_explanation_needed == 'y':
        print('\n')
        print(tictac)
        explain_input()
    input('Let\'s get started! Press enter when you\'re ready.')
    print('\n')
    if robey_marker == 'X':
        row, column = decide_next_move(tictac, robey_marker, new_player.marker)
        tictac.make_move(robey_marker, row, column)
        print(f'\nRobey placed a piece at {row+1}, {column+1}.')

    # Start the game
    while not tictac.check_game_end():
        print(tictac)
        row, column = new_player.prompt_move(tictac)
        tictac.make_move(new_player.marker, row, column)
        print(f'\n{new_player.name} placed a piece at {row+1}, {column+1}.')
        if tictac.check_game_end():
            break
        print(tictac)
        input('Nice move! Robey is next. Press enter when you\'re ready.')
        row, column = decide_next_move(tictac, robey_marker, new_player.marker)
        tictac.make_move(robey_marker, row, column)
        print(f'\nRobey placed a piece at {row+1}, {column+1}.')

    # End game
    result = tictac.announce_game_end()
    if result == new_player.marker:
        print('Wow! You\'ve done the impossible!')
    if result == robey_marker:
        print('Don\'t beat yourself up! Robey\'s a machine. He basically cheats!')
    if result == 'Tie':
        print('Well, a tie is literally the best possible result against Robey, so it\'s kind of like a win. Good job!')


def run_program():
    name = input('Hello, what\'s your name? ')
    print(f'\nWelcome, {name}. Let\'s play some tic tac toe!')
    rules_explanation_needed = input(
        'Would you like me to explain the rules?\nEnter y/n: ').lower()
    while rules_explanation_needed not in ['y', 'n']:
        print('\nSorry, that wasn\'t a valid input. Please enter \'y\' or \'n\'.')
        rules_explanation_needed = input(
            'Would you like me to explain the rules? ').lower()
    if rules_explanation_needed == 'y':
        explain_rules()
    while True:
        # Run a game
        play_tictac(name)
        # Return from game
        go_again = input('\nShall we give it another go?\nEnter y/n: ').lower()
        while rules_explanation_needed not in ['y', 'n']:
            print('\nSorry, that wasn\'t a valid input. Please enter \'y\' or \'n\'.')
            rules_explanation_needed = input(
                'Would you like to play another round? ').lower()
        if go_again == 'n':
            print(
                'Too bad. Robey was having fun! He likes bullying lesser beings.\nCome back anytime!')
            break


run_program()
