from Character_obj import Person
import random
from tkinter import *
from mainwindow import MainWindow


app = MainWindow()

app.mainloop()


# Enemy_list = [Person("soldier"), Person("Kight"), Person("Witch")]

# user_character = Person(input("Please enter the character name : "))
# print("Great! Your character is ready!")
# print(user_character)
# print()

# max_enemies_was = len(Enemy_list)
# while True:
#     if not user_character.IsAlive():
#         print(f"Oh you are dead! you killed {max_enemies_was - len(Enemy_list)} enemies!")
#         break
#     print("Here are the enemies!")

#     for i in Enemy_list:
#         print(i)
    
#     if not Enemy_list:
#         print("Every one was killed! Great job! Bye!")
#         break

#     print("================================")
#     print(f"Your hp {user_character.hp} and xp is {user_character.xp}/{user_character.XP_target}")
#     fight = input("Do you want to fight ? Y/n: ")
#     if fight != "Y":
#         print("Ok. Then next time see ya! Bye!")
#         break

#     Enemy = Enemy_list[random.randint(0, len(Enemy_list) - 1)]
#     print(f"Great! Your enemy is {Enemy.name}")
#     print("Fight begins! \n")
#     while user_character.IsAlive() and Enemy.IsAlive():
#         user_roll = int(input("Please choose number 1 or 2 to attack: "))
#         user_character.Attack(Enemy,user_roll)
#         enemy_roll = random.randint(1,2)
#         Enemy.Attack(user_character, enemy_roll)

#     if not Enemy.is_alive:
#         Enemy_list.remove(Enemy)
