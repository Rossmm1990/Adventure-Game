import sys
import time
from textwrap import dedent

class Character:
  vigor = 10
  strength = 10
  intellect = 10
  dexterity = 10
  luck = 10


class Player(Character):
  pass


def type_writer(text, speed = .01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

class beginning:
  attribute_manaul = {
    "vigor": "how much dmg you do to others",
    "strength": "how much dmg you do to others",
    "intellect": "how much dmg you do to others",
    "dexterity": "how much dmg you do to others",
    "luck": "how much dmg you do to others",
  }

  attribute_list_keys = list(attribute_manaul.keys())

  name = "Ross"

  def attr_map(k, y):
      return f"""{k} determines {y}."""


  read_friendly_attributes_list = map(attr_map, attribute_manaul.keys(), attribute_manaul.values())

  read_friendly_attributes = '\n'.join(read_friendly_attributes_list)
 
  intro_text = (dedent(f"""Well met {name} what kind of skills do you bring to our raiding party?
  Please in the below questions put a number value for each skill that comes up.
  You have a totaly of 20 points to distribute between VIGOR, STRENGTH, INTELLECT,
  DEXTERITY, and LUCK.  If you go over 20 points you will asked to put a different
  amount in till totaly number of points equal 20. \n
  {read_friendly_attributes}\n"""))

  
  def picking_points():
      total_points = 20
      total_points_spent = 0
      for i in attribute_list_keys:
          how_many_points_text =(f"How many points would you like to put in {i} \n")
          type_writer(how_many_points_text)
          points_spent = int(input("> "))
          points_spent_text = (f"You put {points_spent} in {i}\n")
          type_writer(points_spent_text)
          total_points -= points_spent
          total_points_spent += points_spent
          points_left_text = (f"You now have {total_points} points left\n")
          type_writer(points_left_text)
          if total_points_spent > 20:
              to_many_points_text = ("that is too many points lets try that again \n")
              type_writer(to_many_points_text)
              picking_points()


type_writer(intro_text)


