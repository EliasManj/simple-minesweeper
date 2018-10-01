
class Cell:

    FLAG_VALUE = '⚑'
    BOMB_VALUE = '●'
    HIDDEN_VALUE = '-'
    GAME_LOSE = -1

    def __init__(self, revealed, value, x, y):
        self.revealed = revealed
        self.value = value
        self.x = x 
        self.y = y
        self.flagged = False

class Board:

    def __init__(self, **kwargs):
        self.n_bombs = kwargs.get("bombs", 0)
        self.n_rows = kwargs.get("rows", 0)
        self.n_cols = kwargs.get("cols", 0)
        self.size = self.n_rows*self.n_cols
        self.n_valid_cells = self.size - self.n_bombs

    