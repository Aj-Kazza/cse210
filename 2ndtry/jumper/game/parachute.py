class Parachute:
    def __init__(self):
        self._score = 4

    def jump(self):
        if self._score == 4:
            print("  ___ ")
            print(" /___\\")
            print(" \\   /")
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")
        elif self._score == 3:
            print(" /___\\")
            print(" \\   /")
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")
        elif self._score == 2:
            print(" \\   /")
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")
        elif self._score == 1:
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")
        elif self._score == 0:
            print("   x")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")

    def score_number(self, number):
        self._score = number

    def get_score(self):
        return self._score
