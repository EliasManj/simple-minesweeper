
class Board:

    def __init__(self, **kwargs):
        self.n_bombs = kwargs.get("bombs", 0)
        self.n_rows = kwargs.get("rows", 0)
        self.n_cols = kwargs.get("cols", 0)
        self.size = self.n_rows*self.n_cols