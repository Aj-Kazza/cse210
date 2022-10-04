from game.parachute import Parachute
from game.words import Words
from game.guesser import Guesser


class Director:
    def __init__(self):
        self._win = False
        self.guesser = Guesser()
        self.word = Words()
        self.parachute = Parachute()
        self._reveal = []

    def printchute(self):
        self.parachute.jump()

    def getword(self):
        self.word.makeword()

    def makelines(self):
        word = self.word._word
        reveal = list(len(word)*'_')
        self._reveal = reveal

    def guessletter(self):
        self.guesser.guess_letter()


    def lives(self):
        score = self.parachute._score
        print(f"Lives: {score}")

    def start_game(self):
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
        else:
            print(f"Mission Failure, the word was: {self.word._word}")

        