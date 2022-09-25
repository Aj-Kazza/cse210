"""
Ari-John Katia
High Low GAME
CSE 210
"""

#Currently doing all my classes in one file because the current programs on android have trouble trying to read through local modules.


import random

def main():
    director = Director()
    director.start_game()

class Cards:
    """
    Cards class for generating cards
    """
    def __init__(self):
        """
        value for the numerical value of the card
        number for the face number you see on the card, or what we call the cards
        """
        self.value = 0
        self.number = 0
        
    def draw(self):
        """
        draws a random number from 1 to 13 to represent the cards
        """
        value = int(random.randint(1,13))
        self.value = value
        return self.value
        
# decided to add this just to add a little flair to the game but not too much        
    def cardname(self):
        """
        Displays the card's name instead of the number for select cards
        """
        if self.value == 11:
            self.number = "J"
        elif self.value == 12:
            self.number = "Q"
        elif self.value == 13:
            self.number = "K"
        elif self.value == 1:
            self.number = "A"
        else:
            self.number = self.value
            
        return self.number



class Director:
    """
    Director class for directing the game... and stuff, I think there might have been a template or something for the hi-low game last semester or something, because I have no idea where I got the majority of these codes
    """
    
    def __init__(self):
        """
        self.playing - boolean to check if game is running
        self.score - keeps track of the player's score
        self.answered - for debugging purposes to make sure that answers other than required are invalid
        """
        self.playing = True
        self.score = 300
        self.answered = False
        #added this last one for debugging purposes.. okay, not debugging, but I got used to having error messages popping up for when I didn't enter the right stuff so I decided to try to add it into all my codes

            
    def printcard(self):
        """
        prints a card
        """
        if self.playing == False:
            return
        else:
            print(f"The Card is: {Cards.cardname(self)}")
        
    def printnext(self):
        """
        prints the next card
        """
        if self.playing == False:
            return
        else:
            print(f"Next card was: {Cards.cardname(self)}")
        
    def hi_low(self, last, now):
        """
        calculates the high or low by ... calculating the high and low?? err, it does the greater than or less than thingey on the previous card and the current card
        """
        if not self.playing:
            return
        else:
            if now > last:
                return "h"
            elif now < last:
                return "l"
        
    def getansw(self):
        """
        recieves the users answer to high or low
        """
        if self.playing == False:
            return
        else:
            while self.answered != True:
                answer = input("High or Low? [h/l]  ")
                if answer.lower() == "h" or answer.lower() == "l":
                    self.answered = True
                    return answer.lower()
                else:
                    print("Please enter valid value")
            
    def checkansw(self, x, y):
        """
        checks to see if users answer is correct
        """
        if self.playing == False:
            return
        else:
            if x == y:
                self.score = self.score + 100
            else:
                self.score = self.score - 75
            print(f"Current score is: {self.score}")
    
    def play(self):
        """
        checks to see if player wants to play again... that is if you still have points
        """
        if self.playing == False:
            return
        else:
            if self.score > 0:
                while self.answered != True:
                    again = input("Play again? [y/n]  ")
                    if again.lower() == "y":
                        self.playing = True
                        self.answered = True
                    elif again.lower() == "n":
                        self.playing = False
                        self.answered = True
                    else:
                        self.answered = False
                        print("Please enter valid value")
            else:
                print("GAME OVER!! \nYou ran out of points")
    
    def updates(self):
        """
        checks if the program is still running, kind of like Netflix's 'are you still watching?'
        """
        if self.playing == False:
            return
    
    
    def start_game(self):
        """
        starts the game and the program
        """
        while not (self.playing == False or self.score <= 0):
            self.answered = False
            current = Cards.draw(self)
            self.printcard()
            previous = current
            y_answer = self.getansw()
            current = Cards.draw(self)
            self.printnext()
            answer = self.hi_low(previous, current)
            self.checkansw(y_answer, answer)
            self.answered = False
            self.play()
            self.updates()

#only doing this thing because I have no idea how to make this look good and because we talked about it in our group meeting this week so why not
if __name__ == "__main__":
    main()
