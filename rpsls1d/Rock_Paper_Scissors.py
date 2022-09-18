import random


class Game: 
    def __init__(self):
        self.rps = []
        self.rand = ""
        self.answer = ""
        self.hp = 0
        self.enemyhp = 0
        self.enemy = ""
    
    def makeItRandom(self):
        self.rand = random.choice(self.rps)
    
    def print(self):
        print(f"The enemy {self.enemy} Choose ({self.rand})")
        
        
    def letsCheck(self):
        if self.answer == self.rand:
            print("Its a Tie! Go again.")  
            
        elif self.answer == "rock":
            if self.rand == "scissors":
                print("Rock crushes Scissors") 
                self.enemyhp = self.enemyhp - 1
            elif self.rand == "paper": 
                print("Paper covers Rock")
                self.hp = self.hp - 1
            elif self.rand == "lizard":
                print("Rock crushes Lizard")
                self.enemyhp = self.enemyhp - 1
            elif self.rand == "spock":
                print("Spock melts rock")
                self.hp = self.hp - 1    
                       
        elif self.answer == "paper":
            if self.rand == "rock":
                print("Paper covers Rock")
                self.enemyhp = self.enemyhp - 1
            elif self.rand == "scissors":
                print("Scissors cuts Paper")
                self.hp = self.hp - 1
            elif self.rand == "lizard":
                print("Lizard eats paper")
                self.hp = self.hp - 1
            elif self.rand == "spock":
                print("The truth disproves Spock")
                self.enemyhp = self.enemyhp - 1
                
        elif self.answer == "scissors":
            if self.rand == "paper":
                print("Scissors cuts Paper")
                self.enemyhp = self.enemyhp - 1
            elif self.rand == "rock":
                print("Rock crushes Scissors")
                self.hp = self.hp - 1
            elif self.rand == "lizard":
                print("Scissors stab lizard")
                self.enemyhp = self.enemyhp - 1
            elif self.rand == "spock":
                print("do you think scissors can hurt spock?") 
                self.hp = self.hp - 1           
        
        elif self.answer == "lizard":
            if self.rand == "paper":
                print("Lizard eats Paper")
                self.enemyhp = self.enemyhp - 1
            elif self.rand == "rock":
                print("Rock Smashes Lizard")
                self.hp = self.hp - 1
            elif self.rand == "Scissors":
                print("Scissors Stab Lizard")
                self.hp = self.hp - 1
            elif self.rand == "spock":
                print("Lizard Poisons Spock")
                self.enemyhp = self.enemyhp - 1
        
        elif self.answer == "spock":
            if self.rand == "paper":
                print("The truth disproves Spock")
                self.hp = self.hp - 1
            elif self.rand == "rock":
                print("Spock Destroys Rock")
                self.enemyhp = self.enemyhp - 1
            elif self.rand == "scissors":
                print("do you think scissors can hurt spock?")
                self.enemyhp = self.enemyhp - 1
            elif self.rand == "lizard":
                print("Lizard Poisons Spock")
                self.hp = self.hp - 1

    def set_enemy(self):
        enemies = ["goblin", "kobold", "slime", "skeleton", "giant rat", "bandit", "lizardman"]
        enemyrand = random.choice(enemies)
        self.enemy = enemyrand
        if enemyrand == "goblin":
            self.rps = ["rock", "rock", "rock", "rock", "rock", "rock", "paper", "paper", "scissors", "scissors", "scissors", "lizard", "lizard", "lizard", "spock"]
        elif enemyrand == "kobold":
            self.rps = ["rock", "rock", "rock", "rock", "paper", "scissors", "scissors", "scissors", "scissors", "scissors", "lizard", "spock", "spock", "spock", "spock"]
        elif enemyrand == "slime":
            self.rps = ["rock", "rock", "rock", "rock", "rock", "rock", "rock", "paper", "scissors", "scissors", "lizard", "lizard", "lizard", "spock", "spock"]
        elif enemyrand == "skeleton":
            self.rps = ["rock", "paper", "paper", "scissors", "scissors", "scissors", "scissors", "scissors", "scissors", "lizard", "lizard", "lizard", "spock", "spock", "spock"]
        elif enemyrand == "giant rat":
            self.rps = ["rock", "paper", "paper", "paper", "paper", "paper", "paper", "scissors", "scissors", "lizard", "lizard", "lizard", "spock", "spock", "spock"]
        elif enemyrand == "lizardman":
            self.rps = ["rock", "rock", "paper", "scissors", "lizard", "lizard", "lizard", "lizard", "lizard", "lizard", "lizard", "lizard", "lizard", "lizard", "spock"]
        elif enemyrand == "bandit":
            self.rps = ["rock", "paper", "scissors", "lizard", "spock"]

    def calchp(self, hp):
        if hp == 0:
            return "✘ ✘ ✘"
        elif hp == 1:
            return "🎔 ✘ ✘"
        elif hp == 2:
            return "🎔 🎔 ✘"
        elif hp == 3:
            return "🎔 🎔 🎔"

    def resethp(self):
        self.enemyhp = 3
        self.hp = 3


        
def main():
    leave = False
    print("-------------------------------------------------------------")
    print("WELCOME TO---------------------------------------------------")
    title()
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    while leave != True:
        print("1) Play Game\n"
        "2) Intructions\n"
        "3) Quit\n")

        select = input("Select Option: ")

        if select == "3":
            print("\nQUITING.....")
            leave = True
        elif select == "2":
            print("-----------")
            print("How to play")
            print("-----------")
            print("It's just like rock paper scissors, but the one from 'The Big Bang Theory' with a few other stuff in there.")
            print("Both you and your opponent have 3 lives, try your best to survive")
            print("You have learned enough at this point, go out and adventure")
            print()
        elif select == "1":
            print("YOU HAVE DECIDED TO GO TOUCH GRASS!")
            running = True

            while running != False:
                g = Game()
                g.set_enemy()
                g.resethp()
                playing = True

                enc(g.enemy)
                while playing != False:
                    ehp = g.calchp(g.enemyhp)
                    php = g.calchp(g.hp)
                    print()        
                    hud(g.enemy, ehp, php)
                    g.makeItRandom()
                    answer1 = input("Pick one: rock, paper, scissors, lizard, spock:  ")
                    print()
                    g.answer = answer1
                    print()
                    print("You Choose ({})".format(g.answer))
                    print()
                    g.print()
                    print()
                    g.letsCheck()
                    ehp = g.calchp(g.enemyhp)
                    php = g.calchp(g.hp)
                    print()
                    if g.enemyhp == 0:
                        winhud(g.enemy, ehp, php)
                        print()
                        winner()
                        playing = False
                    if g.hp == 0:
                        losehud(g.enemy, ehp, php)
                        print()
                        loser()
                        playing = False

                again = input("Play Again? (y/n)")
                if again.lower() == "y":
                    pass
                elif again.lower() == "n":
                    print("Thus the adventure comes to a close.\n")
                    running = False

        

def hud(enemy, ehp, hp):
    print("-------------------------------------------------------------------------")
    print(f"{enemy.upper()} = {ehp}")
    print("-------------------------------------------------------------------------")
    esprite(enemy)
    txt = (f"PLAYER = {hp}")
    x = txt.center(130)
    print("-------------------------------------------------------------------------")
    print(x)
    print("-------------------------------------------------------------------------")

def winhud(enemy, ehp, hp):
    print("-------------------------------------------------------------------------")
    print(f"{enemy.upper()} = {ehp}")
    print("-------------------------------------------------------------------------")
    winscreen()
    txt = (f"PLAYER = {hp}")
    x = txt.center(130)
    print("-------------------------------------------------------------------------")
    print(x)
    print("-------------------------------------------------------------------------")

def losehud(enemy, ehp, hp):
    print("-------------------------------------------------------------------------")
    print(f"{enemy.upper()} = {ehp}")
    print("-------------------------------------------------------------------------")
    losescreen()
    txt = (f"PLAYER = {hp}")
    x = txt.center(130)
    print("-------------------------------------------------------------------------")
    print(x)
    print("-------------------------------------------------------------------------")

def winner():
    phrases = ["a winner is you!", "winner winner, chicken dinner!", "huzzah, victory!", "yay, you did it!", "enemy vanquished"]
    phrase = random.choice(phrases)
    return print(phrase.upper())

def loser():
    phrases = ["you have been defeated!", "you have fallen in battle", "better luck next time", "you have fainted", "quick, to the pokemon center!"]
    phrase = random.choice(phrases)
    return print(phrase.upper())

def enc(x):
    phrases = [f"You've encountered a wild {x}!", f"Surprise! You are ambushed by a {x}", f"Impossible! There shouldn't be a {x} around these parts!", f"You accidently stumbled upon a {x}, and it's angry!!"]
    phrase = random.choice(phrases)
    return print(phrase)

def esprite(x):
    if x == "skeleton":
        sprite = ("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░█▒▒░░░█░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░█░██▒█░█░██░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░██░░██▌▌▌██░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░██▌░░░█████░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░██░▐███▄█▄█████░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░▐██░▐██▄▄█▄▄▄████████░░░░░░░░░░░\n"
            "░░░░░░░░▐██░▐███▄█▄▄█████▀▀██░░░░░░░░░░░\n"
            "░░░░░░░░▐██▄██░░░██░░░░█▌░░▐█░░░░░░░░░░░\n"
            "░░░░░░░░░█████░██▒████░▐█████░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░░░░░░░░░░\n")
        txt = sprite.center(200)
        print(txt)

    elif x == "bandit":
        sprite = ("░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░██▒██░░██░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░\n"
            "░░░██▄▄░██░░░░░█████░████░░░░░░░░░░░░░░░\n"
            "░░░█▒▒▀███░░▐██░█████████░░░░░░░░░░░░░░░\n"
            "░░░░▌▒░▐███░▐███░████████████░░░░░░░░░░░\n"
            "░░░░█▒░█░███▐█████░██████▀▀██░░░░░░░░░░░\n"
            "░░░░░██░░██████████░██░█▌░░▐█░░░░░░░░░░░\n"
            "░░░░░░░░░█████░██▒████░▐█████░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░░░░░░░░░░")
        txt = sprite.center(200)
        print(txt)

    elif x == "kobold":
        sprite = ("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░█████████░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░███▒░▄░░██░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░███░░░░██░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░██░░░░░█████░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░██░░▐██░████████░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░███░▐███░██░█████████░░░░░░░░░░░\n"
            "░░░░░░░░░███▐█████░██████▀▀██░░░░░░░░░░░\n"
            "░░░░░░░░░██████████░██░█▌░░▐█░░░░░░░░░░░\n"
            "░░░░░░░░░█████░██▒████░▐█████░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░░░░░░░░░░")
        txt = sprite.center(200)
        print(txt)

    elif x == "lizardman":
        sprite = ("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░█████████░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░████▒▒░▄░░██░░░░░░░░░█░░░░░░░░\n"
            "░░░░░░░░░░█████▒░░░██░░░░░░░░░░██▒░░░░░░\n"
            "░░░░░░█░█░░░░░░█████░░░░░░░░░░░░█▒░░░░░░\n"
            "░░░░░█▒███░░▐██▒███▒████░░░░░░░██▒░░░░░░\n"
            "░░░░░█▒▒███░▐██▒▒██▒█████████░██▒▒░░░░░░\n"
            "░░░░░░██░███▐███▒█▒▒█████▒▀████▒▒░░░░░░░\n"
            "░░░░░░░░░███████▒▒▒░██░█▒▒░▐██▒▒░░░░░░░░\n"
            "░░░░░░░░░█████░██▒███████████▒▒░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░░░░░░░░░░")
        txt = sprite.center(200)
        print(txt)

    elif x == "goblin":
        sprite = ("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░█░██▒░░░░██░█░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░███▒▌░▌░███░░░░░░░░░░░░░░░░░\n"
            "░░░░░█████░░░░█▒░░░██░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░█████░░░░░█████░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░█████░░▐██▒▒▒░░████░░░░░░░░░░░░░░░░\n"
            "░░░░░░░████░▐██▒▒░░░█████████░░░░░░░░░░░\n"
            "░░░░░░░░░███▐███▒▒░░█████▒▀███░░░░░░░░░░\n"
            "░░░░░░░░░███████▒▒▒░██░█▒▒░▐██░░░░░░░░░░\n"
            "░░░░░░░░░█████░██▒███████████░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░░░░░░░░░░")
        txt = sprite.center(200)
        print(txt)

    elif x == "slime":
        sprite = ("░░░░░░░░░░░░░░░░░░▄▄▄▄░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░▄█▒▒▒████▄░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░▄█▒▒▒▒▒░░▀████▄░░░░░░░░░░░░░\n"
            "░░░░░░░░░░▄█▒▒▒▒░░░░░░░░█╬███░░░░░░░░░░░\n"
            "░░░░░░░░░█▒▒▒▒░░░░░░░░░╬╬╬╬████░░░░░░░░░\n"
            "░░░░░░░░█▒▒▒░▄░░░░░░░░░▄░╬░░▀███░░░░░░░░\n"
            "░░░░░░░▐▒▒▒▒░██░░░░░░░██░░░░░░███░░░░░░░\n"
            "░░░░░░░█▒▒▒▒░░░░░░░░░░░░░░░░░░░██░░░░░░░\n"
            "░░░░░░░█▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▄██░░░░░░░\n"
            "░░░░░░░▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░░░░\n"
            "░░░░░░░░░░▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        txt = sprite.center(200)
        print(txt)

    elif x == "giant rat":
        sprite = ("░░░░░░░░░░▐██░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░████▄░░░░▄███▄░░░░░░░░░▐█░░░░\n"
            "░░░░░░░░░░░█░░░░▀▀▀▀██░░█░░░░░░░░░▐█▌░░░\n"
            "░░░░░░░░░░░░█░░░░▐█░░░░░░▌░░░░░░░░██░░░░\n"
            "░░░░░░░░░░░▄▄██░░░░░░░██▀░░░░░░▄▄█▀░░░░░\n"
            "░░░░░░░░░██▒▒▀█▀▀▀░░█▀█░▀█░░▄████░░░░░░░\n"
            "░░░░░░░░░██▀▀▀█▒▒░░▐░░░░░░▐███▀░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█▒▒░░█▀▀▀░░░█░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░██▒▒▒▒▒▒▒░▄▀░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░█▀▒▒▒██▀▀██▀▒▀█░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░██▐▒▒██░░░▐▒▒▐▒▄██░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        txt = sprite.center(200)
        print(txt)

def winscreen():
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░╬░░░░░░░░░░░░░░\n"
        "░░░░░░░░░╬╬░░░░░░░░░░░░╬╬╬░░░░░░░░░░░░░░\n"
        "░░░░░░░░░░╬╬╬░░░░░░░╬╬╬▄▄░░░░█▌░░░░░░░░░\n"
        "░░░▐█░░░░░░█▌╬╬▐███▌╬░░███░░░█▌░░░░░░░░░\n"
        "░░░▐█░░█▌░░█▌░░▐███▌░░░████░░█▌░░░░░░░░░\n"
        "░░░▐█░░█▌░░█▌░░▐███▌░░░█▌███░█▌░░░░░░░░░\n"
        "░░░▐█▄▄██▄▄█▌░╬▐███▌╬╬╬█▌░████▌░░░░░░░░░\n"
        "░░░▐████████▌╬╬▐███▌░░╬█▌░░███▌░░░░░░░░░\n"
        "░░░░░░░░░░╬╬╬░░░░░░░░░░░░╬╬╬░░░░░░░░░░░░\n"
        '░░░░░░░░░░╬░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

def losescreen():
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░╬░░░░░░░░░░░░░░\n"
        "░░░░▄░░░░╬▄▄▄▄▄▄▄░░▄▄▄▄▄╬╬░▄▄▄▄▄▄░░░░░░░\n"
        "░░░▐█░░░░░███████░░█████░░░██████░░░░░░░\n"
        "░░░▐█░░░░░█▌╬╬╬▐█░░██▄▄▄▄░░█▌░░░░░░░░░░░\n"
        "░░░▐█░░░░░█▌░░░▐█╬╬██████▌░████░░░░░░░░░\n"
        "░░░▐█░░░░░█▌░░░██╬╬╬░░░░█▌░██▀▀░░░░░░░░░\n"
        "░░░▐█░░░░░█▌░░╬██░▐██████▌░██▄▄▄▄░░░░░░░\n"
        "░░░▐█████░██████▌░░▀▀▀▀▀▀░░██████░░░░░░░\n"
        "░░░░▀▀▀▀▀░▀▀▀▀▀▀░░░░░░░░░╬╬╬░░░░░░░░░░░░\n"
        "░░░░░░░░░░╬░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

def title():
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░█████░░░░░\n"
        "░░███████░░███████░░░█████░░███░░░░░░█████░░███▒▒█░█▒▒▒▒█░░░░\n"
        "░░████░░██░███░░░██░██░░░░█░███░░░░░██░░░░█░█▒▒▒░█░█▒██░░█░░░\n"
        "░░███░░░██░███░░░██░██░░░░░░███░░░░░██░░░░░░███▒░█░█▒█║█░█░░░\n"
        "░░██ROCK██░█PAPER█░░SCISSORS░LIZARD░█SPOCK█░░░█▒░█░█▒█░█░█░░░\n"
        "░░███░███░░███░░░░░░░░░░░██░███░░░░░░░░░░██░░░█▒░█░█▒██░░█░░░\n"
        "░░███░░███░███░░░░░░█░░░░██░███░░░░░█░░░░██░░░█▒░█░█▒▒▒░█░░░░\n"
        "░░███░░░██░███░░░░░░░█████░░███████░░█████░░░░████░█████░░░░░\n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░THE ONE DIMENDSIONAL VER░")

if __name__ == "__main__":
    main()