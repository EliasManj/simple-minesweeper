import os

MENU = 0
GAME = 1
GAME_END = 2
state = 0

def play_game():
    if state == MENU:
        return game_menu()
    elif state == GAME:
        return main_game()
    elif state == GAME_END:
        return end_game()

def game_menu():
    clear_screen()
    print("Commands")
    print("-new game")
    print("-exit")
    user_input = input(">>").strip().lower()
    if user_input == "new game":
        state = GAME
        return True
    elif user_input == "exit":
        return False
    else:
        return True

def exit_game():
    pass

def main_game():
    pass

def end_game():
    pass

def clear_screen():
    clear = lambda: os.system('cls')
    clear()

if __name__ == "__main__":
    status = True
    while status:
        status = play_game()
    exit_game()