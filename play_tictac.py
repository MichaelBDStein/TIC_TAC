from gameboard import Board
from player import Player
from computer_ai import check_win

name = input('Hello, what\'s your name?')
print(f'Welcome, {name}. Let\'s play some tic tac toe!')
while True:
    marker = input(
        'Would you like to be \'X\'s or \'O\'s?\nEnter x/o: ').upper()
    if marker == 'X' or marker == 'O':
        break
    print('Sorry, that\'s not a valid input.\n')
new_player = Player(name, marker)


# tictac = Board(3, 3)
# tictac.make_move(new_player.marker, 2, 2)
# tictac.make_move(new_player.marker, 1, 2)
# tictac.make_move('O', 1, 1)
# tictac.make_move('O', 2, 2)
# tictac.make_move('O', 3, 3)

# print(tictac)
# print(check_win(tictac, 'O'))
