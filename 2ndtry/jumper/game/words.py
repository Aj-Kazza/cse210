import random

class Words:
    """
    Words class: contains word bank and randomizes word
    """
    def __init__(self):
        """
        holds wordbank and word
        """
        self._word = ""
        self.wordbank = ["can", "car", "man", "dog", "fog", "pan", "cat", "key", "mop", "pop",
        "wire", "food", "hand", "book", "raft", "desk", "soda", "mead", "pack", "hill",
        "bread", "peace", "stork", "troll", "spock", "spoon", "print", "slide", "cable", "sugar"]

    def get_word(self):
        """
        returns word
        """
        return self._word

    def makeword(self):
        """
        goes through wordbank and chooses random word
        """
        y = self.wordbank
        x = random.choice(y)
        self._word = x.lower()
        
