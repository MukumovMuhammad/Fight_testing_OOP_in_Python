from Character_obj import Person, Weapon
import random
from tkinter import *
from tkinter import ttk
from mainwindow import Window


Classes = ["Warrior", "Archer", "Wizzard"]
weapons = [Weapon("War Hummer", 5, 25), Weapon("Sword", 4, 20), Weapon("Axe", 2, 10)]


app = Window("Main Window", can_resize=True)

Wellcome_frame = Frame(app)
Wellcome_frame.pack()

def Lets_start():
    if len(inp_name.get()) < 2:
        start_game_lbl.config(text="The name must be at least 2 symbol")
        return
    if not inp_class.get() in Classes:
        start_game_lbl.config(text="Please Choose one of the classes!")
        return
    start_game_lbl.config(text="Great! now choose your weapon!")

    weapon_choose_frame.pack()
    


Label(Wellcome_frame, text="Hello Adventurer! What's your name?").pack()
inp_frames = Frame(Wellcome_frame)
inp_frames.pack()
Label(inp_frames, text="username: ").pack(side=LEFT)
inp_name = Entry(inp_frames, font=("FixedSys", 15))
inp_name.pack(side=LEFT)
inp_frames2 = Frame(Wellcome_frame)
inp_frames2.pack()
Label(inp_frames2, text="choose classes: ").pack(side=LEFT)
inp_class = ttk.Combobox(inp_frames2, values=Classes, font=("FixedSys", 15))
inp_class.pack(side=LEFT)

Button(Wellcome_frame, text="Let's Start!", command=Lets_start).pack()
start_game_lbl = Label(Wellcome_frame, text="")
start_game_lbl.pack()

weapon_choose_frame = Frame(Wellcome_frame)
weapon_choose_frame.pack_forget()
Label(weapon_choose_frame, text="choose weapon: ").pack(side=LEFT)
weapon_cb = ttk.Combobox(weapon_choose_frame, values=weapons, font=("FixedSys", 15))
weapon_cb.pack(side=LEFT)

############# Start of the game #############








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
