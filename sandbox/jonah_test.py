class Item:
  def __init__(self, name, damage, durability):
    self.name = name
    self.damage = damage
    self.durability = durability

p1 = Item('Sword', 10, 100)

print p1.name, p1.damage, p1.durability