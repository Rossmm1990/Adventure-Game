def Intro():
    print("Hello Adventurer! It is time to go raiding with your viking brethen! \n")
    print("Before we set out I will need your name and skills you bring with you \n")

    Name = input("What is your name Adventurer? \n")
    print(f"Well met {Name} what kind of skills to you bring to our raiding party? \n")
    print("""Please in the below questions put a number value for each skill that 
    comes up.  You have a total of 20 points to distribute between VIGOR, strength, 
    INTELLECT, DEXTERITY, and LUCK. If you go over 20 points you will be asked to put
    in a different number till totaly number of points equal 20. /n""")

    vigor_points()

    
def vigor_points():

    vigor_points = input("Vigor determines health, how many points would you like to put in vigor? > \n")
    vigor_points_int = int(vigor_points)

    if vigor_points_int in range(0, 20) and vigor_points_int < 20:
        strength_points()
        
    
    else:
      print("You used to many points! try again")
      health_points() 

def strength_points():
    vigor = vigor_points()

    strength_points = input("""Your strength determines how much dmg you do to others.
    How many points would you like to put in strength? >  \n""")

    strength_points_int = int(strength_points)

    if strength_points_int in range(0, 20) and strength_points_int + vigor_points_int  < 20:
      intellect_points()
    
    else:
      print("You used to many points! try again")
      strength_points()

def intellect_points():

    intellect_points = input("""Your strength determines how much dmg you do to others.
    How many points would you like to put in strength? >  \n""")

    intellect_points_int = int(intellect_points)

    if intellect_points_int in range(0, 20) and strength_points_int + vigor_points_int + intellect_points_int < 20:
      intellect_points()
    
    else:
      print("You used to many points! try again")
      intellect_points()


def dexterity_points():

    dexterity_points = input("""Your strength determines how much dmg you do to others.
    How many points would you like to put in strength? >  \n""")

    dexterity_points_int = int(dexterity_points)

    if dexterity_points_int in range(0, 20) and strength_points_int + vigor_points_int + intellect_points_int + dexterity_points_int < 20:
      dexterity_points()
    
    else:
      print("You used to many points! try again")
      dexterity_points()

def luck_points():

    luck_points = input("""Your strength determines how much dmg you do to others.
    How many points would you like to put in strength? >  \n""")

    luck_points_int = int(luck_points)

    if luck_points_int in range(0, 20) and strength_points_int + vigor_points_int + intellect_points_int + dexterity_points_int + luck_points_int < 20:
      luck_points()
    
    else:
      print("You used to many points! try again")
      luck_points()   

class beginning:
  attribute_pool = 20

  attribute_manaul = {
    "vigor": "how much dmg you do to others",
    "strength": "how much dmg you do to others",
    "intellect": "how much dmg you do to others",
    "dexterity": "how much dmg you do to others",
    "luck": "how much dmg you do to others",
  }

  

  

class Character:
  def __init__(self, vigor, strength, intellect, dexterity, luck):
    self.vigor = 10 + vigor
    self.strength = strength
    self.intellect = intellect
    self.dexterity = dexterity
    self.luck = luck


class Player(Character):
  pass

Ross = Character(5, 10, 10, 10, 10)

print(Ross.vigor)





