""" Deck settings """
from enum import Enum
class SUIT(Enum):
    Spades = 0
    Diamonds = 1
    Clubs = 2
    Hearts = 3

SUITS = [SUIT.Diamonds, SUIT.Clubs, SUIT.Hearts, SUIT.Spades]

DECK_SIZE = 52
VALUE = {
    "A":1,
    "K":13,
    "Q":12,
    "J":11,
}

for val in range(2,11):
    VALUE[str(val)]=val

""" Player/Lobby settings """
DEFAULT_LOBBY_SIZE = 4
HAND_SIZE = 5
MAX_LOBBY_SIZE = DECK_SIZE // HAND_SIZE
