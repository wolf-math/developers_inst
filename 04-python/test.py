from datetime import datetime

cake = '''
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''

user_birthday = input("what is your birthday? (DD/MM/YYYY) ")

user_birthday = user_birthday[6: ]

age = datetime.now().year - int(user_birthday)

last_digit = age % 10

candle_space = "       "

number_of_spaces = 11 - last_digit
number_of_spaces = number_of_spaces / 2

candles = (int(number_of_spaces) * '_') + ("i" * last_digit) + (int(number_of_spaces) * '_')

print(candle_space + candles  + cake)

