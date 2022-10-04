from parachute import Parachute
from words import Words
from guesser import Guesser


class Director:
    def __init__(self):
        self._score = 4
        self._win = False
        self.guesser = Guesser
        self.word = Words
        self.parachute = Parachute
        self._reveal = []

    def printchute(self):
        self.parachute.jump(self)

    def getword(self):
        self.word.banklvl(self)
        self.word.makeword(self)

    def makelines(self):
        word = self.word.word
        reveal = list(len(word)*'_')
        self._reveal = reveal

    def guessletter(self):
        self.guesser.guess_letter(self)

    def updates(self):
        self._win = self.guesser.check_letter(self, self.word.word, self._reveal)

    def start_game(self):
        while self._win == False and self._score > 0:
            self.getword()
            self.makelines()
            self.printchute()
            self.guessletter()
            self.updates()


        