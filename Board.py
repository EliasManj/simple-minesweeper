from random import shuffle

class Cell:

    FLAG_VALUE = '⚑'
    BOMB_VALUE = '●'
    HIDDEN_VALUE = '-'
    GAME_LOSE = -1

    def __init__(self, value, x, y):
        self.revealed = False
        self.value = value
        self.x = x 
        self.y = y
        self.flagged = False

    def is_bomb(self):
        return self.value == Cell.BOMB_VALUE

    def print_cell_debug(self):
        return str(self.value)

class Board:

    def __init__(self, **kwargs):
        self.n_bombs = kwargs.get("bombs", 0)
        self.n_rows = kwargs.get("rows", 0)
        self.n_cols = kwargs.get("cols", 0)
        self.size = self.n_rows*self.n_cols
        self.n_valid_cells = self.size - self.n_bombs
        self.create_random_board()

    def create_random_board(self):
        self.board = [Cell.BOMB_VALUE]*self.n_bombs + [0]*self.n_valid_cells
        shuffle(self.board)
        self.board = [self.board[i:i+self.n_cols] for i in range(0, self.size, self.n_rows)]
        for row in range(0,self.n_rows):
            for col in range(0,self.n_cols):
                self.board[row][col] = Cell(value=self.board[row][col], x=row, y=col)
        self.print_board_debug()

    def fill_cells(self):
        for row in range(0,self.n_rows):
            for col in range(0,self.n_cols):
                if not self.board[row][col].is_bomb(): 
                    self.count_bombs(self.board[row][col])

    def count_bombs(self, cell):
        assert cell.value != Cell.BOMB_VALUE
        
    def print_board_debug(self):
        for row in self.board:
            print(list(map(lambda x: x.print_cell_debug(), row)))

    