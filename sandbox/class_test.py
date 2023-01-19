
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





