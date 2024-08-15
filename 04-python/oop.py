# class Dog():
#     def __init__(self, name, age, color, noise):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.noise = noise

#     def bark(self):
#         return f"{self.name} goes {self.noise} late at night"
    
#     def eat(self, food):
#         return f"{self.name} eats {food}. YUM! YUM!"
    
#     def change_color(self, new_color):
#         self.color = new_color
#         print(f"{self.name}'s color was changed to {new_color}")


# bobby = Dog("Robert", 4, "brown", "woof")
# luna = Dog("Luna", 3, "black and white", "OOoooOOOoo")
# peanut = Dog("Peanut Butter", 8, "brown", "Snort")

# print(bobby.color)
# bobby.change_color('grey')



# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

#   def rename(self):
#     new_name = input("What's my new name? ")
#     if not new_name.isdigit():
#         self.name = new_name


# first_person = Person("John", 36)
# first_person.show_details()

# first_person.rename()
# first_person.show_details()

# first_person.name = 'Freddy'
# first_person.show_details()



class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)
# prints "Apple"

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")

# prints "I am a computer, my name is Mark" x2
