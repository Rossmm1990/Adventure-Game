import random

class player:
	def __init__(self, name):
		self.name = name
	strength = 14
	dexterity = 14
	constition = 10
	intellgence = 10
	wisdom = 10
	charisma = 10
	armor = 14
	health = 100


	skills = [] 
	inventory = []

	def add_item_to_inventory(self, item_name, character_name):
		character_name.inventory.append(item_name)

	def add_skill(self, skill_name, character_name):
		character_name.skills.append(skill_name)


class enemy:

	def __init__(self, health, dmg, roll_to_hit, roll_to_dodge, initiative, name):
		self.health = health
		self.dmg = dmg
		self.roll_to_hit = roll_to_hit
		self.roll_to_dodge = roll_to_dodge
		self.initiative = initiative
		self.name = name

		
class skills:

	def __init__(self, skill_dmg, skill_name):
		self.skill_dmg = skill_dmg
		self.skill_name = skill_name
		

class item:
	def __init__(self, item_dmg, name):
		self.name = name	
		self.item_dmg = item_dmg

	def equip_item(self, player, item):
		pass	
	

	
class battle_engine:

	
	def initiative_roll(player, enemy):
		initiative_roll = (player.dexterity -10)/2 + random.randint(0, 20)
		
		if initiative_roll > enemy.initiative:
			initiative = 1
			print(f"{player.name} goes first")
			input("hit enter to continue")
			return initiative
		else:
			initiative = 2
			print(f"{enemy.name} goes first\n")
			input("hit enter to continue")
			return initiative

	def skill_roll(player_name, player_skill_name, player_skill):
		skill_roll_value = (player_skill -10) + random.randint(0, 20)
		print(f"{player_name.name} rolled a {skill_roll_value} for {player_skill_name}")
		input("hit enter to continue\n")
		return skill_roll_value
	
	def enemy_attack(enemy_name, player_name):
		dmg = enemy_name.dmg
		print(f"{enemy_name.name} attacks and does {dmg} dmg")
		print(f"You now have {player_name.health - dmg} health\n")
		return dmg

	def player_attack(player_name, enemy_name):
		dmg = player_name.inventory[0].item_dmg + player_name.skills[0].skill_dmg
		print(f"You attack with {player_name.skills[0].skill_name} and does {dmg} dmg")
		print(f"The {enemy_name.name} now has {enemy_name.health - dmg} health\n")
		return dmg 

		
		
	def type_of_attack():
		pass
		





Ross = player("Ross")
melee_attack = skills(5, "melee_attack")
ranged_attack = skills(5, "melee_attack")
sword = item(5, "sword")
bow = item(5, "bow")
Ross.inventory.append(sword)
farmer = enemy(100, 5, 7, 7, 20, "farmer")
warrior_1 = enemy(150, 5, 10, 8, 20, "bill")
x ="print"

Ross.add_item_to_inventory(sword, Ross)
Ross.add_skill(melee_attack, Ross)







def fighting_the_farmer(player_name, enemy_name):
	print("You come across a farmer with a pitchfork do you fight him?\n")
	yes_fight = input("type yes or no >")

	if yes_fight == "yes":
		print("you draw your sword, lets see who goes first")
	elif yes_fight == "no":
		print("You run away")
		end()
	else:
		print("type yes or no you dummy")
		fighting_the_farmer(player_name, enemy_name)

	initiative = battle_engine.initiative_roll(player_name, enemy_name)

	if initiative == 2:

		while player_name.health and enemy_name.health >= 0:

			player_dmg = battle_engine.enemy_attack(enemy_name, player_name)
			player_name.health -= player_dmg

			input("hit enter to continue >\n")

			if_hit = battle_engine.skill_roll(player_name, "strength", player_name.strength)

			if if_hit > enemy_name.roll_to_hit:
				enemy_dmg = battle_engine.player_attack(player_name, enemy_name)
				enemy_name.health -= enemy_dmg
				input("hit enter to continue")
			else:
				print(f"You missed! your strenth roll was not high enough you need a {enemy_name.roll_to_hit} to hit!\n")
				input("hit enter to continue > \n")

	if player_name.health >= 0:
		print(f"you defeated the{enemy_name.name}")
	else:
		print(f"you were defeated by the {enemy_name.name}")


fighting_the_farmer(Ross, farmer)			
















