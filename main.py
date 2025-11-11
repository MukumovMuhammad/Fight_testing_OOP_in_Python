from Character_obj import Person
import random

Enemy_list = [Person("soldier"), Person("Kight"), Person("Witch")]

user_character = Person(input("Please enter the character name : "))
print("Great! Your character is ready!")
print(user_character)
print()



while user_character.IsAlive():
    print("Here are the enemies!")
    alived_enemies = 0
    for i in Enemy_list:
        alived_enemies += i.is_alive
        print(i)
    
    if not alived_enemies:
        print("Every one was killed! Great job! Bye!")
        user_character.Die()

        
    fight = input("Do you want to fight ? Y/n: ")
    if fight != "Y":
        print("Ok. Then next time see ya! Bye!")
        user_character.Die()

    Enemy = Enemy_list[random.randint(0, len(Enemy_list) - 1)]
    print(f"Great! Your enemy is {Enemy.name}")
    print("Fight begins! \n")
    while user_character.IsAlive() and Enemy.IsAlive():
        user_roll = int(input("Please choose number 1 or 2 to attack: "))
        user_character.Attack(Enemy,user_roll)
        enemy_roll = random.randint(1,2)
        Enemy.Attack(user_character, enemy_roll)


