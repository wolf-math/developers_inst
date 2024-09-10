import random
from time import sleep

rps = ['rock','paper','scissors']

class Game():
    def __init__(self):
        self.computer_item = 'rock'
        self.user_input = 'rock'
        self.game_data = []

    def get_user_item(self):
        while True:
            user_input = input('Pick [rock/paper/scissors]: ')
            if user_input in rps:
                self.user_input = user_input
                break
            else:
                print("that wasn't an option")
        
    def get_computer_item(self):
        self.computer_item = random.choice(rps)

    def get_game_reslt(self):
        choice_number = rps.index(self.user_input)
        computer_choice = rps.index(self.computer_item)

        if choice_number == computer_choice:
            print(f"Player: {self.user_input}, Computer: {self.computer_item}.")
            print("Draw")
            self.game_data.append('draw')
        elif choice_number == (computer_choice + 1) % 3:
            print(f"Player: {self.user_input}, Computer: {rps[computer_choice]}.")
            print("PLAYER WINS!")
            self.game_data.append('win')
        else:
            print(f"Player: {self.user_input}, Computer: {rps[computer_choice]}.")
            print("COMPUTER WINS!")
            self.game_data.append('loss') 


    def play(self):
        self.get_computer_item()
        self.get_user_item()
        print("")
        print(f"Computer plays {self.computer_item}.\n")
        self.get_game_reslt()
        print("")
        sleep(1)


        
