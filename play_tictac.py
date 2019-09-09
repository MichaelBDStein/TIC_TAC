from gameboard import *
from player import *
from computer_ai import *


def play_tictac():
    name = input('Hello, what\'s your name?')
    print(f'Welcome, {name}. Let\'s play some tic tac toe!')
    while True:
        marker = input(
            'Would you like to be \'X\'s or \'O\'s?\nEnter x/o: ').upper()
        if marker == 'X' or marker == 'O':
            break
        print('Sorry, that\'s not a valid input.\n')
    new_player = Player(name, marker)
    # if new_player.marker == 'X':
    #     new_robot = 'O'  # FIX THIS
    # if new_player.marker == 'O':
    #     new_robot = 'X'  # FIX THIS
    tictac = Board(3, 3)
    tictac.make_move('X', 0, 0)
    tictac.make_move('X', 2, 1)

    # Start the game
    while not tictac.check_game_end():
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
