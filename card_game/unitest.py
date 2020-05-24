import deck
import settings

def evaluateHand(hand) -> int:
    handScore = 0
    cardsPerSuit = [[] for x in settings.SUITS]
    onlyValue = []
    score1, score2, score3, score4, score5 = 0, 0, 0, 0, 0
    for card in hand:
        cardValue = settings.VALUE[card.val]

        # add rule 1 score
        score1 += cardValue
        # extract the numerical values from all cards in hand
        onlyValue.append(cardValue)
        # group all cards with the same suit
        cardsPerSuit[card.suit.value].append(cardValue)

    for suit in cardsPerSuit:
        sameSuitCards = len(suit)
        if sameSuitCards > 1:
            # adding rule 3 score
            score3 += sameSuitCards * min(suit)
    print(cardsPerSuit)

    rule2 = 0
    rule4 = 0
    onlyValue.sort()
    i = 0
    inc = False
    while i < len(onlyValue):
        # find how many cards have the same numerical value
        while i+1 < len(onlyValue) and (onlyValue[i+1] == onlyValue[i]):
            rule2 += 1
            i += 1
            inc = True
        # Adding rule 2 score
        if rule2 > 0:                
            score2 = onlyValue[i-1]**(rule2+1)
            rule2 = 0

        # find how many cards have the sequential numerical values
        while i+1 < len(onlyValue) and (onlyValue[i+1] - onlyValue[i] == 1):
            rule4 += 1
            i += 1
            inc = True
        # Adding rule 4 score
        if rule4 > 0:
            score4 += (rule4+1)*onlyValue[i]
            rule4 = 0
            
        if inc == True:
            inc = False
        else:
            i += 1

    print(onlyValue)
    # Adding rule 5 score
    score5 += (onlyValue[-1] - onlyValue[0])

    handScore = score1+score2+score3+score4+score5

    print("Player has score {}".format(handScore))
    print("Analytical score:")
    print("Score1 " + str(score1))
    print("Score2 " + str(score2))
    print("Score3 " + str(score3))
    print("Score4 " + str(score4))
    print("Score5 " + str(score5))
    print()
    return handScore

assert evaluateHand(
    [deck.Card(settings.SUIT.Spades,"8"),
    deck.Card(settings.SUIT.Hearts,"7"),
    deck.Card(settings.SUIT.Diamonds,"Q"),
    deck.Card(settings.SUIT.Hearts,"2"),
    deck.Card(settings.SUIT.Spades,"Q")]
) == 231

assert evaluateHand(
    [deck.Card(settings.SUIT.Spades,"10"),
    deck.Card(settings.SUIT.Clubs,"J"),
    deck.Card(settings.SUIT.Hearts,"A"),
    deck.Card(settings.SUIT.Clubs,"8"),
    deck.Card(settings.SUIT.Hearts,"2")]
) == 86

assert evaluateHand(
    [deck.Card(settings.SUIT.Hearts,"9"),
    deck.Card(settings.SUIT.Diamonds,"6"),
    deck.Card(settings.SUIT.Hearts,"3"),
    deck.Card(settings.SUIT.Clubs,"K"),
    deck.Card(settings.SUIT.Hearts,"7")]
) == 71

assert evaluateHand(
    [deck.Card(settings.SUIT.Diamonds,"10"),
    deck.Card(settings.SUIT.Clubs,"10"),
    deck.Card(settings.SUIT.Spades,"10"),
    deck.Card(settings.SUIT.Spades,"K"),
    deck.Card(settings.SUIT.Hearts,"4")]
) == 1076

assert evaluateHand(
    [deck.Card(settings.SUIT.Spades,"10"),
    deck.Card(settings.SUIT.Spades,"Q"),
    deck.Card(settings.SUIT.Spades,"K"),
    deck.Card(settings.SUIT.Spades,"9"),
    deck.Card(settings.SUIT.Spades,"J")]
) == 169