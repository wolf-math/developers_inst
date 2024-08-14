import random

def random_word_index(length):
    rand_index_list = []
    for _ in range(length):
        rand_index_list.append(random.randrange(267751))
    return rand_index_list


def get_specific_line(line_number):
    with open('words-list.txt', 'r') as file:
        lines = file.readlines()
    return lines[line_number - 1].strip()

def main(length):
    sentence = ''
    indeces = random_word_index(length)
    for i in indeces:
        sentence += (get_specific_line(i) + ' ')
    return sentence


print(main(4))