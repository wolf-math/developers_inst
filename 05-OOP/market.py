# class Farm():
#     def __init__(self, name):
#         self.name = name
#         self.animals = {}

#     def add_animal(self, animal, number=1):
#         if animal in self.animals:
#             self.animals[animal] += number
#         else:
#             self.animals[animal] = number

#     def get_info(self):
#         for animal in self.animals.keys():
#             print(f'{animal} : {self.animals[animal]}')

#         return 'E I E I O'


# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())

# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

#     def shrink(self, factor=2):
#         self.diameter = self.diameter / factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)

# nc.grow()

# print(nc.diameter)

# nc.shrink()

# print(nc.diameter)

class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super().func()

my_instance_2 = ChildClass()
my_instance_2.func()