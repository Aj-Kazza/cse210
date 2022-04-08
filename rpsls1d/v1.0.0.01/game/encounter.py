import random

class phrases():
    def __init__(self):
        self.win = ""
        self.encounter = ""
        self.lose = ""

    def winner(self):
        phrases = ["a winner is you!", "winner winner, chicken dinner!", "huzzah, victory!", "yay, you did it!", "enemy vanquished"]
        phrase = random.choice(phrases)
        self.win = (phrase.upper())

    def loser(self):
        phrases = ["you have been defeated!", "you have fallen in battle", "better luck next time", "you have fainted", "quick, to the pokemon center!"]
        phrase = random.choice(phrases)
        self.lose = (phrase.upper())

    def enc(self, x):
        if x == "gelatinous cube":
            self.encounter = f"OH NO! You have stumbled upon the {x} and now are in despair!\n You did not sign up for this!! QUICKLY RUN!!"
        else:
            phrases = [f"You've encountered a wild {x}!", f"Surprise! You are ambushed by a {x}", f"Impossible! There shouldn't be a {x} around these parts!", f"You accidently stumbled upon a {x}, and it's angry!!"]
            phrase = random.choice(phrases)
            self.encounter = phrase

    def getwin(self):
        return self.win

    def getlose(self):
        return self.lose

    def getenc(self):
        return self.encounter