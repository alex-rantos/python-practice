import deck
import lobby

if __name__ == "__main__":
    deck = deck.Deck()
    lobby = lobby.Lobby()
    while(True):

        deck.shuffle()

        lobby.setDealer()

        lobby.handOut(deck.deck)
        lobby.getWinner()
        
        userInput = input('Type "exit" to stop the game. Insert anything else to continue!')

        if (userInput == "exit"):
            exit()
        
        lobby.gatherCards(deck.deck)
        print(deck)
        print(len(deck.deck))
        print(lobby)

