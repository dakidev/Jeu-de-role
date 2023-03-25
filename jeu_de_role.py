from random import randint

enemy = 50
start = 50
potions_number = 3
skip = False

while True:
    if skip:
        print("Vous passez votre tour...😕")
        skip = False
    else:
        user_input = ""
        while not (user_input.isdigit() and int(user_input) in range(3)):
            user_input = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
            
        user_input = int(user_input)
        if user_input == 1: 
            your_attack = randint(5, 10)
            enemy -= your_attack
            print(f"Vous avez infligé {your_attack} points de dégats à l'ennemi ⚔️")
        elif user_input == 2 and potions_number > 0: 
            potion = randint(15, 50)
            start += potion
            potions_number -= 1
            skip = True
            print(f"Vous récupérez {potion} points de vie ❤️ ({potions_number} ? restantes)")
        else:
            print("Vous n'avez plus de potions...")
            continue
    
    if enemy <= 0:
        print("🎊🎉Tu as gagné !!!👏👏👏")
        break

    enemy_attack = randint(5, 15)
    start -= enemy_attack
    print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")

    if start <= 0:
        print("Tu as perdu 😢")
        break

    print(f"Il vous reste {start} ❤️  points de vie.")
    print(f"Il reste {enemy} ❤️  points de vie à l'ennemi.")
    print("*-" * 30 )

print("Fin du jeu.")