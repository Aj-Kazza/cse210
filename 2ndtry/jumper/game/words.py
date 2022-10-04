import random

class Words:
    def __init__(self):
        self._word = ""
        self._wordbank = []

    def get_word(self):
        return self._word

    def banklvl(self):
        x = random.randint(3,5)
        if x == 3:
            self._wordbank["can", "car", "man", "dog", "fog", "pan", "cat", "key", "mop", "pop"]
        elif x == 4:
            self._wordbank["wire", "food", "hand", "book", "raft", "desk", "soda", "mead", "pack", "hill"]
        elif x == 5:
            self._wordbank["bread", "peace", "stork", "troll", "spock", "spoon", "print", "slide", "cable", "sugar"]

    def makeword(self):
        y = self._wordbank
        x = random.choice(y)
        self._word = x.lower()
        
