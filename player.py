class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def prompt_move(self, board):
        while True:
            position_input = input(
                'Where would you like to place your next piece? ')
            split_input = position_input.split()
            if len(split_input) != 2:
                print(
                    'Invalid input. Please give exactly two elements: row position and column position.')
                continue
            try:
                row = int(split_input[0]) - 1
                column = int(split_input[1]) - 1
            except ValueError:
                print('Invalid input. Please enter numbers only.')
                continue
            if row not in range(board.rows) or column not in range(board.columns):
                print(
                    'Invalid input. Please choose values within the range of the board.')
                continue
            position_tuple = (row, column)
            if position_tuple not in board.available_spaces:
                print(
                    'That space is already taken. Please choose an empty spot on the board.')
                continue
            return row, column
