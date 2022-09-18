from game import Game
from enemy import enemy
from hud import hud
import screens
import encounter

def main():
    leave = False
    print("-------------------------------------------------------------")
    print("WELCOME TO---------------------------------------------------")
    screens.title()
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
                p = encounter.phrases()
                h = hud()


                p.enc()
                while playing != False:
                    ehp = g.calchp(g.enemyhp)
                    php = g.calchp(g.hp)
                    print()        
                    h.normal(ehp, php)
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
                        h.win(ehp, php)
                        print()
                        p.winner()
                        playing = False
                    if g.hp == 0:
                        h.lose(ehp, php)
                        print()
                        p.loser()
                        playing = False

                again = input("Play Again? (y/n)")
                if again.lower() == "y":
                    pass
                elif again.lower() == "n":
                    print("Thus the adventure comes to a close.\n")
                    running = False

        
if __name__ == "__main__":
    main()