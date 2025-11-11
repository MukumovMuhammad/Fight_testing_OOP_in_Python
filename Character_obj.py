
import random

class Person:
    def __init__(self, name : str):
        self.name = name
        self.hp = 10
        self.is_alive = True
    
    def Attack(self,enemy, roll):
        if not self.IsAlive():
            return
        self_roll = random.randint(1,2)

        if roll == self_roll:
            print(f"The {self.name} damaged the {enemy.name}")
            enemy.Hit(2)
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
    

    def __str__(self):
        return(f"name : {self.name}, hp : {self.hp}")

