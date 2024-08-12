
# def hello(greeting, name="jimmmy"):
#     if greeting == "hello":
#         return f"Goodbye {name}"
#     else:
#         return f"{greeting} {name}"

# greet = hello("hello", "Posidon")

# print(greet)

# greetings_list = [greet]

# print(greetings_list)

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician)

# def calculation(*args):
#     print(args)
#     total = 0
#     for i in args:
#         total += i
    
#     difference = args[0]
#     for i in range(1, len(args)):
#         difference -= args[i]

#     return (total, difference)

# big_number, small_number = calculation(77,105, 100, 1, 1234, 99)

# print(big_number)
# print(small_number)


# def  check_keywordedarguments(fav_book, *args, **kwargs):
#     print(fav_book)
#     print(args)
#     print(kwargs)

# check_keywordedarguments('the odyssey',1,2,3,4, name="Sarah", age=24)

# def upper_string(s):
#     return s.upper()

# def starts_with_A(s):
#     return s[0] == "A"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filtered_object = filter(starts_with_A, fruit)

# print(list(filtered_object))

def name_size(name):
    return len(name)<=4

def greet(name):
    return f"hello {name}"

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

filtered = filter(name_size, people)
mapped = list(map(greet, filtered))

print(mapped)


"""LAMBDA WAY"""

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered = filter(lambda name: len(name)<=4, people)
mapped = list(map(lambda short_name: f"hello {short_name}", filtered ))

print(mapped)

