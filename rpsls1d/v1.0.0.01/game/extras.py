#extra functions that I can't seem to find a place for them in the other files
import random
from game.enemy import goblin, kobold, slime, skeleton, giant_rat, bandit, lizardman, cube

def setenemy():
    enemies = ["goblin", "kobold", "slime", "skeleton", "giant rat", "bandit", "lizardman", "cube"]
    enemyrand = random.choice(enemies)
    if enemyrand == "goblin":
        return goblin()
    elif enemyrand == "kobold":
        return kobold()
    elif enemyrand == "slime":
        return slime()
    elif enemyrand == "skeleton":
        return skeleton()
    elif enemyrand == "giant rat":
        return giant_rat()
    elif enemyrand == "bandit":
        return bandit()
    elif enemyrand == "lizardman":
        return lizardman()
    elif enemyrand == "cube":
        return cube()
