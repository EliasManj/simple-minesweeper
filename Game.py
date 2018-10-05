from Board import Board
import os
import re

class Game:

    MENU = 0
    GAME = 1
    GAME_END = 2
    NEW_GAME = 3
    DEBUG = 0
    state = 0
    board = None
    msg = ""
    x_re = re.compile(r"\d+(?=,)")
    y_re = re.compile(r"(?<=,)\d+")

    def main_loop(self):
        self.status = True
        while self.status:
            self.status = self.play_game()
        self.exit_game()

    def play_game(self):
        if self.state == Game.MENU:
            return self.game_menu()
        elif self.state == Game.GAME:
            return self.main_game()
        elif self.state == Game.NEW_GAME:
            return self.new_game()
        elif self.state == Game.GAME_END:
            return self.end_game()

    def game_menu(self):
        self.clear_screen()
        print("Commands")
        print("-new game")
        print("-exit")
        user_input = input(">>").strip().lower()
        if user_input == "new game":
            self.state = Game.NEW_GAME
            return True
        elif user_input == "exit":
            return False
        else:
            return True

    def new_game(self):
        self.clear_screen()
        print("Choose dificulty")
        print("-easy (4x4)")
        print("-medium (9x9)")
        print("-hard (16x16)")
        user_input = input(">>").strip().lower()
        if user_input == "easy":
            self.board = Board(bombs=10, rows=4, cols=4)
            self.state = Game.GAME
        elif user_input == "medium":
            self.board = Board(bombs=10, rows=9, cols=9)
            self.state = Game.GAME
        elif user_input == "hard":
            self.board = Board(bombs=10, rows=16, cols=16)
            self.state = Game.GAME
        return True

    def exit_game(self):
        pass

    def main_game(self):
        self.prompt_user()
        return True

    def end_game(self):
        self.clear_screen()
        print(self.msg)
        self.board.print_board_debug()

    def prompt_user(self):
        self.clear_screen()
        print(self.msg)
        self.print_board()
        print("Commands:")
        print("-mine x,y")
        print("-flag x,y")
        user_input = input(">>").strip().lower()
        if user_input.startswith("mine"):
            self.mine(user_input)
        elif user_input.startswith("flag"):
            pass
        else:
            pass
        return

    def mine(self, user_input):
        x_str, y_str = self.parse_x_y(user_input)
        if x_str and y_str:
            x = int(x_str.group(0))
            y = int(y_str.group(0))
            if x > 0 and x <= self.board.n_rows and y > 0 and y <= self.board.n_cols:
                self.msg = "Mining {},{}".format(x, y)
                if not self.board.mine_cell(x-1, y-1):
                    self.state = self.GAME_END
                    self.msg = "You lost"

    def parse_x_y(self, user_input):
        return [re.search(self.x_re, user_input), re.search(self.y_re, user_input)]

    def clear_screen(self):
        def clear(): return os.system('cls')
        clear()

    def print_board(self):
        if self.DEBUG:
            self.board.print_board_debug()
        else:
            self.board.print_board_show_bombs_only()