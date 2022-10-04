
class Guesser:
    def __init__(self):
        self._guess = ""
        self._score = 4

    def check_letter(self, word, reveal):
        guess = self._guess
        for i in range(0,len(word)):
            letter = word[i]
            if guess == letter:
                reveal[i] = guess
        if "_" not in reveal:
            return True
        else:
            return False


    def guess_letter(self):
        guess = input("Guess a letter [a-z]:    ")
        self._guess = guess
