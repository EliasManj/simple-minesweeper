from Board import Board

class Game:

    MENU = 0
    GAME = 1
    GAME_END = 2
    NEW_GAME = 3
    state = 0
    board = None
    
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
        print("Choose dificulty")
        print("-easy (4x4)")
        print("-medium (9x9)")
        print("-hard (16x16)")
        user_input = input(">>").strip().lower()
        if user_input == "easy":
            self.board = Board(bombs=10, rows = 4, cols = 4)
        elif user_input == "medium":
            self.board = Board(bombs=10, rows = 9, cols = 9)
        elif user_input == "hard":
            self.board = Board(bombs=10, rows = 16, cols = 16)

    def exit_game(self):
        pass

    def main_game(self):
        pass

    def end_game(self):
        pass

    def clear_screen(self):
        clear = lambda: os.system('cls')
        clear()