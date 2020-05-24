import settings
import random

class Deck:
    def __init__(self):
        self.__size = settings.DECK_SIZE
        self.deck = []
        for suit in settings.SUITS:
            for card_id in settings.VALUE:
                self.deck.append(Card(suit,card_id))

    def __str__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

class Card:
    def __init__(self, suit, val:int):
        self.suit = suit
        self.val = str(val)

    def __str__(self):
        return "[" + str(self.suit) + " " + self.val + "]"
        
    def __repr__(self):
        return str(self)