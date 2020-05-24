import settings
import random


class Lobby:
    lobby = []
    __size = 0

    def __init__(self, size=settings.DEFAULT_LOBBY_SIZE):
        if (size < 2):
            self.__size = 2
        elif (size >= settings.MAX_LOBBY_SIZE):
            self.__size = settings.MAX_LOBBY_SIZE
        else:
            self.__size = size
        for player in range(1, self.__size + 1):
            self.lobby.append(Player(player))

    def __str__(self):
        return str(self.lobby)

    def setDealer(self, player=-1):
        if player in range(1, self.__size + 1):
            self.dealer = player
        else:
            self.dealer = random.randint(1, self.__size)

    def handOut(self, deck):
        for i in range(5):
            for player in self.lobby:
                card = deck.pop()
                player.receiveHard(card)
                if (i == 4):
                    print(player)

    def getWinner(self):
        maxScore = 0
        winner = []
        for player in self.lobby:
            score = player.evaluateHand()

            if (score > maxScore):
                maxScore = score
                if len(winner) > 0:
                    winner.clear()
                winner.append(player.getId())
            elif (score == maxScore):
                winner.append(player.getId())

        print("Highest score is: " + str(maxScore))
        if len(winner) == 1:
            print("Winner is Player#" + str(winner[0]))
        elif (len(winner)) > 1:
            print("DRAW between players: " + str(winner))

    def gatherCards(self,deck):
        for player in self.lobby:
            print(player.getId())
            print(player.hand)
            deck.extend(player.hand)
            player.hand.clear()
            print(player.hand)



class Player:
    def __init__(self, id):
        self.__id = str(id)
        self.hand = []
        self.score = 0

    def getId(self):
        return self.__id

    def receiveHard(self, card):
        self.hand.append(card)

    def evaluateHand(self) -> int:
        handScore = self.score
        cardsPerSuit = [[] for x in settings.SUITS]
        onlyValue = []
        score1, score2, score3, score4, score5 = 0, 0, 0, 0, 0
        for card in self.hand:
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

        # Adding rule 5 score
        score5 += (onlyValue[-1] - onlyValue[0])

        handScore = score1+score2+score3+score4+score5

        print("Player {} has score {}".format(self.__id, handScore))
        print("Analytical score:")
        print("Score1 " + str(score1))
        print("Score2 " + str(score2))
        print("Score3 " + str(score3))
        print("Score4 " + str(score4))
        print("Score5 " + str(score5))
        print()
        return handScore

    def __str__(self):
        return "Player:[" + self.__id + "] has:" + str(self.hand)

    def __repr__(self):
        return str(self)

