from game.parachute import Parachute
from game.words import Words
from game.guesser import Guesser


class Director:
    """
    obligatory Director class: holds the stuff together and runs the game
    """
    def __init__(self):
        """
        ._win - sees if the game is won (boolean)
        .guesser - intance of Guesser classes
        .word - instance of Words class
        .parachute - instance of Parachute classes
        ._reveal - list of separated letters of .words._word
        """
        self._win = False
        self.guesser = Guesser()
        self.word = Words()
        self.parachute = Parachute()
        self._reveal = []

    def printchute(self):
        """
        grabs the parachute sprite prints from the parachute class
        """
        self.parachute.jump()

    def getword(self):
        """
        gets words from the words class
        """
        self.word.makeword()

    def makelines(self):
        """
        creats a list of stuff that tracks the guess progress from words._word
        """
        word = self.word._word
        reveal = list(len(word)*'_')
        self._reveal = reveal

    def guessletter(self):
        """
        grabs the guess letter function to guess the letter
        """
        self.guesser.guess_letter()

    #for debugging purposes
    def lives(self):
        """
        calculates the score and edits the parachute score
        """
        score = self.parachute._score
        print(f"Lives: {score}")

    def start_game(self):
        """
        Starts the game
        """
        self.getword()
        self.makelines()
        print(' '.join([str(l) for l in self._reveal]))
        print()
        self.printchute()
        print()
        while self._win == False and self.parachute._score > 0:
            self.guessletter()
            print()
            if len(self.guesser._guess) == 1 and self.guesser._guess in self.word._word:
                self._win = self.guesser.check_letter(self.word._word, self._reveal)
            else:
                self.parachute._score -= 1
            print(' '.join([str(l) for l in self._reveal]))
            print()
            self.printchute()
            print()

        if self._win:
            print("CONGRATULATION!")
            print() 
        else:
            print(f"YOU FELL! \nthe word was: {self.word._word}")
            print()

        