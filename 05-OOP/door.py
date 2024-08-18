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

class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')

class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')

if __name__ == '__main__':
    foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
    foundation.present()
    print(foundation.price)
    print(foundation.bored)
    boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
    print(boring_book.bored)