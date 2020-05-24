# About

A card game developed in python 3.8.3. Earlier version of python 3 should be fine too.

Each turn 4 (default value can be changed in settings.py) players are created and draw 1 card each till they all get 5. The highest scoring hand wins.

# Invocation

```python ./game.py ``` 

## Explanation

Heavy OOP approach: Every bit of the game functionality is broken down to classes. A brief file explanation:

* game.py: The main game interface.
* deck.py: Deck interface which contains Deck and Card classes. The deck is a 52-length list of unique Card objects.
* lobby.py: Contains Lobby and Player classes and follows the same structure as deck; a lobby is a list of Players. Includes all game's logic.
* settings.py: Saved constants for easier configuration.
* unitest.py: Includes the examples (hardcoded) from the .pdf to confirm the validity of the evaluation function.