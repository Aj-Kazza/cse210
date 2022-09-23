from game.cards import Cards
import random

class Director:


    def __init__(self):


        self.cards = []
        self.is_playing = True
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while not (self.is_playing == False or self.score <= 0):
            current = Cards.draw(self)
            self.printcard(current)
            previous = current
            y_answer = self.get_answer()
            current = Cards.draw(self)
            self.printnext(current)
            answer = self.hi_low(previous, current)
            self.check_answers(y_answer, answer)
            self.play()
            self.do_updates
            
    def current(self):
        if not self.is_playing:
            return 
        else:
            Cards.draw(self)

    def printcard(self, card):
        if not self.is_playing:
            return 
        else:
            print(f"The Card is: {card}")

    def printnext(self, card):
        if not self.is_playing:
            return 
        else:
            print(f"Next card was: {card}")


    def hi_low(self, last, now):
        if not self.is_playing:
            return 
        else:

            if now > last:
                return "h"
            elif now < last:
                return "l"

    def get_answer(self):
        if not self.is_playing:
            return
        else:
            answer = input("High or Low? [h/l] ")
            return answer.lower()

    def check_answers(self, x, y):
        if not self.is_playing:
            return 
        else:
            if x == y:
                self.score = self.score + 100
            else:
                self.score = self.score - 75
            print(f"Current score is: {self.score}")

    def play(self):
        if not self.is_playing:
            return 
        else:

            if self.score > 0:
                again = input("Play again? [y/n]")
                self.is_playing = (again == "y")
            else:
                print("GAME OVER!! \nyou ran out of points")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 


 
