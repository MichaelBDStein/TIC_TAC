class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [['_' for i in range(columns)] for i in range(rows)]
        self.available_spaces = [(x, y) for x in range(rows)
                                 for y in range(columns)]

    def __repr__(self):
        board_string = ''
        for row in self.board:
            for column in row:
                board_string += str(column) + '|'
            board_string = board_string[:-1]
            board_string += '\n'
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
            print('Game over. \'O\' wins!')
            return 'O'
        if self.check_win('X'):
            print('Game over. \'X\' wins!')
            return 'X'
        if not self.available_spaces:
            print('Game over. It\'s a tie.')
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
