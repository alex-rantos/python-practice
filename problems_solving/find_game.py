"""Solve the game "Guess a number", find a secret integer between 1 and 1000000
in less than 50 guesses. Write a function that solves the game without user input and returns the
solution by using the function verify() which is defined with the following
specification:
function verify(guess: integer) -> integer
Argument:
     guess (integer) the number to verify
Returns:
     0 if the guess is the solution, your program won
     -1 if the solution is smaller than the guess parameter
     1  if the solution is bigger than the guess parameter

Warning: You are not allowed to call verify() more that 50 times or you loose."""
import random
EXIT_CODE = -100
class Guess_number(object):
    
    def __init__(self, secret_int = None):
        self.counter = 0
        if (secret_int == None):
            self.secret_int = random.randint(1, 1000000)
        else:
            if isinstance(secret_int, int) and secret_int in range(1,1000001):
                self.secret_int = secret_int
            else:
                raise Exception("Secret int must be between 1 and 1000000. Invalid input :[%s]".format(secret_int))
    
    def verify(self, guess: int) -> int:   
        if self.counter >= 50:
            print("Cannot guess anymore")
            return EXIT_CODE    
        if guess < self.secret_int:
            return (-1)
        elif guess > self.secret_int:
            return (1)
        else:
            return (0)
        self.counter += 1
    
    def play_game_without_user(self) -> bool:
        played = set([])
        low , high = 1, 1000000
        for i in range(50):
            guess = random.randint(low, high)
            while guess in played:
                guess = random.randint(low, high)
            played.add(guess)
            res = self.verify(guess)
            if res == 0:
                print("BEAT THE GAME")
                return True
            elif res == 1:
                high = guess
            elif res == -1:
                low = guess
        print("Game over :(")
        return False

if __name__ == "__main__":
    g = Guess_number(500)
    g.play_game_without_user()