from game.game import rps
from game.hud import hud
import game.screens
import game.encounter
import game.extras

def main():
    leave = False
    print("-------------------------------------------------------------")
    print("WELCOME TO---------------------------------------------------")
    game.screens.title()
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    while leave != True:
        print("1) Play Game\n"
        "2) Intructions\n"
        "3) Quit\n"
        "P) Patch Notes\n")

        select = input("Select Option: ")

        if select == "3":
            print("\nQUITING.....")
            leave = True
        elif select.lower() == "p":
            print(
                "---------\n"
                "V1.0.0.01\n"
                "---------\n"
                "+New code formatting and even more files!!\n"
                "+Optimized for PC\n"
                "+Changed HP to HP bar for UNICODE unsupported devices\n"
                "+Added 2 new hidden mechanics!! What are they? ¯\\_(ツ)_/¯\n"
                "+NEW ENEMY!! Can you defeat the newly added boss!?")
            print()
        elif select == "2":
            print("-----------")
            print("How to play")
            print("-----------")
            print("+It's just like rock paper scissors, but the one from 'The Big Bang Theory' \nwith a few other stuff in there.")
            print("+Both you and (most of) your opponent have 3 lives, try your best to survive.")
            print("+You have learned enough at this point, go out and adventure.")
            print()
        elif select == "1":
            print("YOU HAVE DECIDED TO GO TOUCH GRASS!")
            running = True

            while running != False:
                g = rps()
                opponent = game.extras.setenemy()
                opp = opponent
                g.resethp(opp.maxhp)
                playing = True
                p = game.encounter.phrases()
                h = hud()
                opsp = opp.setsprite()
                g.enemy = opp.name
                g.run = 0

                p.enc(g.enemy)
                print(p.getenc())
                while playing != False:
                    ehp = g.calchp(g.enemyhp)
                    php = g.calchp(g.hp)
                    print()        
                    h.normal(g.enemy, ehp, opsp, php)
                    opp.setattack()
                    g.rand = opp.getattack()
                    answer1 = input("Pick one: rock, paper, scissors, lizard, spock:  ")
                    print()
                    g.answer = answer1
                    print()
                    print("You Choose ({})".format(g.answer))
                    print()
                    g.turn()
                    print()
                    g.letsCheck()
                    print()
                    if g.enemyhp == 0:
                        h.win(g.enemy, php)
                        print()
                        p.winner()
                        print(p.getwin())
                        playing = False
                    elif g.hp == 0:
                        h.lose(g.enemy, ehp)
                        print()
                        p.loser()
                        print(p.getlose())
                        playing = False
                    elif g.run == 1:
                        playing = False

                answering = False
                while not answering:
                    again = input("Play Again? (y/n) ")
                    if again.lower() == "y":
                        answering = True
                    elif again.lower() == "n":
                        print("Thus the adventure comes to a close.\n")
                        running = False
                        answering = True
                    else:
                        pass

        
if __name__ == "__main__":
    main()