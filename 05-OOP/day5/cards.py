import random

class Deck():
    def __init__(self):
        suits = ['♦', '♣', '❤', '♠']
        values = ['a', 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,'j', 'q', 'k']
        self.deck = self.deck = [Card(suit, value) for suit in suits for value in values]

    def show_deck(self):
        for card in self.deck:
            print(card)

    def shuffle(self):
        self.deck = sorted(self.deck, key=lambda x: random.random())

    def deal(self):
        a = self.deck.pop()
        print(a)

class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return f"{self.value} {self.suit}"



a = Deck()
a.shuffle()
a.deal()
a.show_deck()