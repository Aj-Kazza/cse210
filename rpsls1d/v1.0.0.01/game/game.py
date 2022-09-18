import random

class rps: 
    def __init__(self):
        self.rps = []
        self.rand = ""
        self.answer = ""
        self.hp = 0
        self.enemyhp = 0
        self.enemy = ""
        self.maxhp = 3
        self.run = 0

    
    def turn(self):
        print(f"The enemy {self.enemy} chose ({self.rand})")
        
        
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

        elif self.answer == "run":
            print("You decided to flee")
            run = random.randint(1, 10)
            if run >= 5:
                print("You succesfully fled the battle, nice!")
                self.run = 1
            else:
                print("Your flee is failed, big oof!")
                self.hp = self.hp - 1
                self.run = 0

        else:
            print("You did a feint! Sneaky ain't ya!?")

    def calchp(self, maxhp):
        calc = []
        for i in range(maxhp):
            calc.append("█")
        point = str(' '.join(calc))
        return point
        

    def resethp(self, enemymaxhp):
        self.enemyhp = enemymaxhp
        self.hp = self.maxhp