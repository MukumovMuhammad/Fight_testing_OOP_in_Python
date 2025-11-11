
import random

class Person:
    
    def __init__(self, name : str):
        self.name = name
        self.max_hp = 10
        self.hp = self.max_hp
        self.is_alive = True
        self.xp = 0
        self.level = 1
        self.XP_target = 10
    
    def Attack(self,enemy, roll):
        if not self.IsAlive():
            return
        self_roll = random.randint(1,2)

        if roll == self_roll:
            print(f"The {self.name} damaged the {enemy.name}")
            enemy.Hit(2)
            self.earnedXP(2)
        else:
            print(f"The {self.name} coudn't hit the {enemy.name}")

    def IsAlive(self):
        if self.is_alive:
            return True
        print(f"The {self.name} is Dead!")
        return False

    def Hit(self, damage : int):
        self.hp = self.hp - damage
        print(f"{self.name}'s hp is {self.hp} ")
        if self.hp <= 0:
            self.Die()
    
    def Die(self):
        self.is_alive = False
    
    def earnedXP(self, xp: int):
        self.xp += xp
        if self.xp >= self.XP_target:
            self.UpgradeLevel()
            
    def UpgradeLevel(self):

        self.level += 1
        self.max_hp += self.max_hp * 0.5
        self.hp = self.max_hp
        self.XP_target = self.level *  12
        print(f"{self.name} level was upgraded to {self.level}")


    def __str__(self):
        return(f"name : {self.name}, hp : {self.hp}, level : {self.level}")

