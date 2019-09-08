class Board:
    def __init__(self, rows, columns):
        self.board = [['_' for i in range(columns)] for i in range(rows)]

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
        if self.board[row-1][column-1] != '_':
            print('That space is already taken.')
            return
        self.board[row-1][column-1] = f'{marker}'
