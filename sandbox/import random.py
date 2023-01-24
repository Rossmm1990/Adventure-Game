import random


class Player:
    def __init__(self, name):
        self.name = name

    strength = random.randint(0, 20)
    dexterity = random.randint(0, 20)
    constition = random.randint(0, 20)
    intellgence = random.randint(0, 20)
    wisdom = random.randint(0, 20)
    charisma = random.randint(0, 20)
    armor = random.randint(0, 20)
    health = random.randint(0, 20)


Master_player_names_list = [
    "Olaf",
    "Udyr",
    "Ragnar",
    "Utred",
    "Appa",
    "Eric",
    "Sigmond",
    "Thorin",
    "Holfsed",
    "Beorn",
]

player1 = Player(random.choice(tuple(Master_player_names_list)))

print(player1.name)
print(player1.name)
print(player1.name)
print(player1.name)

 