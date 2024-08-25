from game import Game

def get_user_menu_choice():
    print("Choose \n1) Play Game\n2) Get Stats\n3) Quit")
    choice = input(">>> ")
    return choice

def print_results(results):
    pass

def main():
    while True:
        game = Game()
        choice = get_user_menu_choice()
        if choice == '1':
            game.play()
        if choice == '2':
            game.get_game_reslt()
        if choice == '3':
            break


if __name__ == "__main__":
    main()
