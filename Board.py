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
        self.show_value = '-'

    def is_bomb(self):
        return self.value == Cell.BOMB_VALUE

    def print_cell_debug(self):
        return str(self.value)

    def print_cell_show_bomb(self):
        if self.is_bomb():
            return str(self.value)
        else:
            return str(self.show_value)

    def mine(self):
        if self.is_bomb():
            return False
        else:
            self.reveal()
        return True

    def reveal(self):
        if not self.revealed:
            self.show_value = self.value
            

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
        self.fill_cells()

    def fill_cells(self):
        for row in range(0,self.n_rows):
            for col in range(0,self.n_cols):
                if not self.board[row][col].is_bomb():
                    self.count_bombs(self.board[row][col])

    def get_cell_value(self, x, y):
        return self.board[x][y].value

    def get_cell_list(self, positions):
        return [self.get_cell_value(x,y) for x,y in positions]


    def count_bombs(self, cell):
        assert cell.value != Cell.BOMB_VALUE
        row = cell.x
        col = cell.y
        if self.is_top_border_cell(cell) and self.is_right_border_cell(cell):
            adjacent_cells = self.get_cell_list([(row-1,col),(row-1, col+1),(row, col+1)])
        elif self.is_top_border_cell(cell) and self.is_left_border_cell(cell):
            adjacent_cells = self.get_cell_list([(row+1,col),(row+1, col+1),(row, col+1)])
        elif self.is_bottom_border_cell(cell) and self.is_left_border_cell(cell):
            adjacent_cells = self.get_cell_list([(row,col-1),(row+1, col-1),(row+1, col)])
        elif self.is_bottom_border_cell(cell) and self.is_right_border_cell(cell):
            adjacent_cells = self.get_cell_list([(row-1, col-1),(row-1, col),(row, col-1)])
        elif(self.is_border_cell(cell)):    
            if self.is_top_border_cell(cell):
                adjacent_cells = self.get_cell_list([(row-1, col),(row-1, col+1),(row, col+1),(row+1, col+1),(row+1, col)])          
            elif self.is_bottom_border_cell(cell):
                adjacent_cells = self.get_cell_list([(row-1, col),(row-1, col-1),(row, col-1),(row+1, col-1),(row+1, col)])
            elif self.is_right_border_cell(cell):
                adjacent_cells = self.get_cell_list([(row, col-1),(row-1, col-1),(row-1, col+1),(row-1, col),(row, col+1)])
            elif self.is_left_border_cell(cell):
                adjacent_cells = self.get_cell_list([(row, col-1), (row+1, col-1), (row+1, col), (row+1, col+1), (row, col+1)])
        else:
            adjacent_cells = self.cell_get_neighbors(cell)
        cell.value = adjacent_cells.count(Cell.BOMB_VALUE)

    def cell_get_neighbors(self, cell):
        neighbors = self.cell_get_bottom(cell)+self.cell_get_top(cell)+self.get_cell_list([(cell.x-1, cell.y),(cell.x+1, cell.y)])
        return neighbors

    def is_top_border_cell(self, cell):
        return cell.y == 0

    def is_bottom_border_cell(self, cell):
        return cell.y >= self.n_rows - 1
    
    def is_right_border_cell(self, cell):
        return cell.x >= self.n_cols - 1
    
    def is_left_border_cell(self, cell):
        return cell.x == 0

    def is_border_cell(self, cell):
        return self.is_bottom_border_cell(cell) or self.is_top_border_cell(cell) or self.is_left_border_cell(cell) or self.is_right_border_cell(cell)

    def cell_get_top(self, cell):
        return [self.board[cell.x-1][cell.y-1].value, self.board[cell.x][cell.y-1].value, self.board[cell.x+1][cell.y-1].value]

    def cell_get_bottom(self, cell):
        return [self.board[cell.x-1][cell.y+1].value, self.board[cell.x][cell.y+1].value, self.board[cell.x+1][cell.y+1].value]
    
    def cell_get_right(self, cell):
        return [self.board[cell.x+1][cell.y-1].value, self.board[cell.x+1][cell.y].value, self.board[cell.x+1][cell.y+1].value]

    def cell_get_left(self, cell):
        return [self.board[cell.x-1][cell.y-1].value, self.board[cell.x-1][cell.y].value, self.board[cell.x-1][cell.y+1].value]
        
    def mine_cell(self, x, y):
        return self.board[x][y].mine()

    def print_board_debug(self):
        for row in self.board:
            print(list(map(lambda x: x.print_cell_debug(), row)))

    def print_board_show_bombs_only(self):
        for row in self.board:
            print(list(map(lambda x: x.print_cell_show_bomb(), row)))