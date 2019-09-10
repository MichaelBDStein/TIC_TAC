class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [['_' for i in range(columns)] for i in range(rows)]
        self.available_spaces = [(x, y) for x in range(rows)
                                 for y in range(columns)]

    # Prints a human-readable form of the board, without changing how the data is stored.
    # Adds numbers to the right and bottom sides of the board to indicate row and column number.
    # Currently, going beyond 10 columns will misalign the column markers, since the labels become 2 digits wide.
    def __repr__(self):
        board_string = ''
        row_label = 0
        for row in self.board:
            for column in row:
                board_string += str(column) + '|'
            board_string = board_string[:-1]
            row_label += 1
            board_string += f' {row_label}\n'
        column_labels = ''
        for i in range(self.columns):
            column_labels += f'{i+1} '
        board_string += column_labels
        return board_string

    def __getitem__(self, key):
        return self.board[key]

    def make_move(self, marker, row, column):
        if self.board[row][column] != '_':
            print('That space is already taken.')
            return
        self.board[row][column] = f'{marker}'
        self.available_spaces.remove((row, column))

    def check_game_end(self):
        if self.check_win('O'):
            return 'O'
        if self.check_win('X'):
            return 'X'
        if not self.available_spaces:
            return 'Tie'

    # The same function as check_game_end, but with print statements.
    # Separated so that I could control flow without necessarily printing.
    def announce_game_end(self):
        if self.check_win('O'):
            print('\nGame over. \'O\' wins!')
            print(self)
            return 'O'
        if self.check_win('X'):
            print('\nGame over. \'X\' wins!')
            print(self)
            return 'X'
        if not self.available_spaces:
            print('\nGame over. It\'s a tie.')
            print(self)
            return 'Tie'

    # This is a weak solution for check win state.
    # It's the same as simply running 8 if true statements for the 8 possible 3-in-a-rows. I just made it a little bit cuter.
    # I intend on increasing the intelligence of this, so that it can handle larger boards and varying lengths for the winning run.
    def check_win(self, marker):
        winning_rows = [[(0, 0), (0, 1), (0, 2)], [
            (1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]
        winning_columns = [[(0, 0), (1, 0), (2, 0)], [
            (0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
        winning_diagonals = [[(0, 0), (1, 1), (2, 2)], [
            (0, 2), (1, 1), (2, 0)]]
        for row in winning_rows:
            win = True
            for x, y in row:
                if self[x][y] != marker:
                    win = False
            if win:
                return True
        for col in winning_columns:
            win = True
            for x, y in col:
                if self[x][y] != marker:
                    win = False
            if win:
                return True
        for diag in winning_diagonals:
            win = True
            for x, y in diag:
                if self[x][y] != marker:
                    win = False
            if win:
                return True
        return False
