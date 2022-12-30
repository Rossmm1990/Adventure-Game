#created dictionary called inventory
inventory = {"stick": "Stick"}

# function that adds item from game into the inventory dictionary
def add_inv(item, item_abr):
    inventory[f"{item_abr}"] = item

# fucntion open_inv to see what is in inventory and return whatevr you choose to equip
def open_inv():
    print("You open your inventory and look a the contents")
    print("Your inventory contains...")
    print(','.join(inventory.keys()))
    print("Select item by typing name of item")
    selected = input("> ")
    in_hand = inventory[f'{selected}']
    return in_hand

# fucntion that tells you what you equipped!
def equip_item():
    equipped = open_inv()
    print(f"You equipped a {equipped}")

# calls function open_inv
open_inv()

# calls function open equip_teim
equip_item()



print("You come across a sword! Do you pick it up?")

pick_up = input("Type yes or no > ")

# if statement for if you picked up sword if yes assigns sword to two variables then runs add_inv function using the two variables
if pick_up == "yes":
    a = "Sword"
    b = "sword"
    add_inv(a, b)
else:
    print("You leave the sword on the ground")

open_inv()

equip_item()



