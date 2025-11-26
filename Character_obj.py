
import random


class Weapon:

    def __init__(self, name : str, demage: int = 1, manna_takes = 0):
        self.name = name
        self.demage = demage
        self.manna_takes = manna_takes

    def Attack(self ,enemy):
        enemy.Hit(self.demage)
    
    def __str__(self):
        return f"{self.name} manna value {self.manna_takes}"

class Person:
    def __init__(self, name : str, weapon : Weapon = Weapon(name="hands")): # type: ignore
        self.name = name
        self.max_hp = 10
        self.hp = self.max_hp
        self.is_alive = True
        self.xp = 0
        self.level = 1
        self.XP_target = 10
        self.weapon = weapon
        self.manna = 100
        self.max_manna = 100
    
    def Attack(self,enemy, roll):
        if not self.IsAlive() or self.manna - self.weapon.manna_takes < 0:
            return
        self_roll = random.randint(1,2)
        self.manna -= self.weapon.manna_takes
        if roll == self_roll:
            print(f"The {self.name} damaged the {enemy.name}")
            self.weapon.Attack(enemy)
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
        self.max_manna += self.max_manna * 0.5
        self.manna = self.max_manna
        print(f"{self.name} level was upgraded to {self.level}")

    def UpdateFromOneRound(self):
        self.manna += random.randint(1,20)
        if self.manna > self.max_manna: self.manna = self.max_manna

    def __str__(self):
        return(f"name : {self.name}, hp : {self.hp}, level : {self.level}, manna : {self.manna}")
