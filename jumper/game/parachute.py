class Parachute:
    def __init__(self):
        self.score = 4

    def disp(self):
        if self.score == 4:
            print(" ___ ")
            print("/___\\")
            print("\\   /")
            print(" \\ /")
            print("  0")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")
        elif self.score == 3:
            print("/___\\")
            print("\\   /")
            print(" \\ /")
            print("  0")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")
        elif self.score == 2:
            print("\\   /")
            print(" \\ /")
            print("  0")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")
        elif self.score == 1:
            print(" \\ /")
            print("  0")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")
        elif self.score == 0:
            print("  x")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")

    def score_number(self, number):
        self.score = number

