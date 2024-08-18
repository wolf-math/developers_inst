"""
We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

We can create a class called BlockedDoor that inherits from the base class Door.

We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version 
of those functions, which simply raises an Error that a blocked door cannot be opened or closed.
"""

# class Door:
#     def __init__(self, is_opened = True):
#         self.is_opened = is_opened

#     def open_door(self):
#         self.is_opened = True

#     def close_door(self):
#         self.is_opened = False


# class BlockedDoor(Door):
#     def open_door(self):
#         raise ValueError('A blocked door cannot be opened.')
    
#     def close_door(self):
#         raise ValueError('A blocked door cannot be closed.')


# blocked = BlockedDoor()
# blocked.close_door()
# blocked.open_door()


# my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

# total = 0
# for number in my_list:
#     try:
#         total += number
#     except:
#         continue

# print(total)


z = 9
try:
    assert 1 == z
except AssertionError:
    print("Error: Those are not equals")