# fruits = ['apple', 'banana', 'kiwi', 'pear']

# for fruit in fruits:
#   print(fruit)

# cities = ["Tel Aviv", "San Francisco", "Paris", "Barcelona"]

# for city in cities:
#     print(f"I once went to {city}")



# for i in range(5,10):
#     print(i)


# num_list = [1,2,3,4,5,10]
# # num_list_sum = sum(num_list)

# total = 0
# for i in num_list:
#     print('i', i)
#     total += i
#     print('total', total)

# print('final result', total)

# number = input("gimme a number! ")

# for i in range(1,11):
#     print(int(number) * i)

# password = ''
# while password != 'hello-world-123':
#   password = input('What is the top secret password? ')

# print('You guessed the right password!')


# while True: 
#     city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
#     if city == 'quit':
#         break
#     elif city == 'leave me alone':
#         break
#     elif city == 'stop':
#         break
#     else:
#         print("I'd love to go to", city)

# print("Goodbye !")

import random
num = random.random()
num *= 1000

guesses = 1

while guesses <=5:
    number = int(input("guess a number between 1 and 1000: "))
    if number == int(num):
        print("you got it!")
        break
    elif number < num:
        print("too low")
    elif number > num:
        print("too high")
    
    guesses += 1

print(f"you guessed {guesses} times.")
print(f"the number is {num}.")