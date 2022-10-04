
class Guesser:
    """
    Guesser class: contains the guess, and probably that one thing to make the "_" thing work
    """
    def __init__(self):
        """
        holds the guess variable
        """
        self._guess = ""

    #got this from youtube, somehow managed to make it work on its own
    def check_letter(self, word, reveal):
        """
        checks letter: arg:
        - checks with word, which is supposed to connect two words._word
        - connects with separated word list to show correcponding correct letters
        """
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
        """
        inputs the guess and holds it as a variable
        """
        guess = input("Guess a letter [a-z]:    ")
        self._guess = guess
