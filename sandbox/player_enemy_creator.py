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

    inventory = {}

    def add_item_to_inventory(self, item_name, character_name):
        character_name.inventory.append(item_name)

    skills = {}

    def add_skill(self, skill_name, character_name):
        character_name.skills.append(skill_name)


class Enemy:
    def __init__(
        self,
        name,
        strength,
        dexterity,
        constition,
        intellegence,
        wisdom,
        charisma,
        armor,
        health,
    ):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constition = constition
        self.intellegence = intellegence
        self.wisdom = wisdom
        self.charisma = charisma
        self.armor = armor
        self.health = health

    def add_item_to_inventory(self, item_name, character_name):
        character_name.inventory.append(item_name)

    def add_skill(self, skill_name, character_name):
        character_name.skills.append(skill_name)

    skills = {}
    inventory = {}


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

farmer = Enemy("farmer", 10, 10, 10, 10, 10, 10, 10, 50)
soldier = Enemy("soldier", 15, 15, 10, 10, 10, 10, 15, 100)
knight = Enemy("knight", 20, 20, 10, 10, 10, 10, 20, 150)

player1 = Player(random.choice(Master_player_names_list))
player2 = Player(random.choice(Master_player_names_list))
player3 = Player(random.choice(Master_player_names_list))
player4 = Player(random.choice(Master_player_names_list))
player5 = Player(random.choice(Master_player_names_list))

Master_player_dict = {
    player1.name: player1,
    player2.name: player2,
    player3.name: player3,
    player4.name: player4,
    player5.name: player4,
}

Master_enemy_list = {farmer.name: farmer, soldier.name: soldier, knight.name: knight}

print(Master_player_dict)
