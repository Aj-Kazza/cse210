import random

class Words:
    def __init__(self):
        self._word = ""
        self.wordbank = ["can", "car", "man", "dog", "fog", "pan", "cat", "key", "mop", "pop",
        "wire", "food", "hand", "book", "raft", "desk", "soda", "mead", "pack", "hill",
        "bread", "peace", "stork", "troll", "spock", "spoon", "print", "slide", "cable", "sugar"]

    def get_word(self):
        return self._word

    def makeword(self):
        y = self.wordbank
        x = random.choice(y)
        self._word = x.lower()
        
