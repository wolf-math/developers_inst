import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'creditcard', 'rush', 'south']
word = random.choice(wordslist) 

def check_word(letter):
    if letter in word:
        return True
    else:
        return False
    
def place_letter(letter, incomplete_word):
    
    incomplete_list = list(incomplete_word)
    print(incomplete_word, incomplete_list)
    for count, char in enumerate(word):
        if letter == char:
            print(count)
            print(char)
            incomplete_list[count] = letter

    return "".join(incomplete_list)
        

def check_win():
    pass

def print_board():
    pass

def get_user_input(guessed_letters):
    while True:
        user_input = input("guess a letter: ")

        if user_input.isdigit():
            print('invalid')
        elif user_input in guessed_letters:
            print('you did that already')
        elif user_input not in word:
            return (user_input, False)
        else:
            return (user_input, True)


def play():
    wrong_guesses = 0
    guessed_letters = []
    incomplete_word = len(word) * "*"
    while wrong_guesses <= 6:
        print(incomplete_word)
        guess = get_user_input(guessed_letters)

        guessed_letters.append(guess[0])

        if guess[1] == False:
            wrong_guesses += 1
        else:
            incomplete_word = place_letter(guess[0], incomplete_word)

        print(incomplete_word)
        print(guessed_letters)

        if incomplete_word == word:
            print("you win")
            break


play()