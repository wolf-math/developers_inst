# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def __init__(self, sounds, name, age):
#         super().__init__(name, age)
#         self.sounds = sounds
    
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def __init__(self, sounds, name, age):
#         super().__init__(name, age)
#         self.sounds = sounds

#     def sing(self, sounds):
#         return f'{sounds}'


# # Create another cat breed named Siamese which inherits from the Cat class.
# # Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# # Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# # Take all the cats for a walk, use the walk method.
# class Siamese(Cat):
#     def __init__(self, sounds, name, age):
#         super().__init__(name, age)
#         self.sounds = sounds

#     def sing(self):
#         return self.sounds

# bengal = Bengal("roar", "Banjo", 32)
# char = Chartreux("meow", "Charlie", 12)
# sia = Siamese("eew", "Herbert", 5)

# all_cats = [bengal, char, sia]


# sara_pets = Pets(all_cats)

# sara_pets.walk()

# from pcode import PythonCoding

# pcode = PythonCoding("Python")
# jscode = PythonCoding("JavaScript")



# import random

# class Dot:
#     def __init__(self, alive, x, y):
#         self.alive = alive
#         self.x = x
#         self.y = y

# board = []
# for i in range(10):
#     column = []
#     for j in range(10):
#         column.append(Dot(random.choice([True, False]), i, j))
#     board.append(column)

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    
    def __iadd__(self, other):
        try:
            self.amount += other.amount
        except:
            self.amount += other

        return self

    def __add__(self, other):
        try:
            if self.currency != other.currency:
                raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')
            return self.amount + other.amount
        except:
            return self.amount + other
        
    def __int__(self):
        return self.amount
    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1)
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>