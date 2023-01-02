import random

master_item_list = ["sword", "axe", "shield", "spear", "bucket of poop"]
master_item_dict = {"sword": "sword", "axe": "axe", "shield": "sheild", "spear": "spear", "bucket of poop": "bucket of poop"}
inventory = {"stick": "stick", "cucumber": "cucumber"}
inventory_list = ["stick", "cucumber"]

item_list = random.choice(tuple(master_item_list))
item_dict = random.choice(list(master_item_dict.items()))






# function that adds item from game into the inventory dictionary
def add_inv(item, item_abr):
    inventory[f"{item_abr}"] = item

# fucntion open_inv to see what is in inventory and return whatevr you choose to equip
def open_inv_list():
    print("You open your inventory and look a the contents")
    print("Your inventory contains...")
    print(','.join(inventory_list))
    print("Select item by typing number of item")
    selected = input("> ")
    in_hand = inventory_list[(int(selected))]
    equip_item(in_hand)
    

# fucntion open_inv to see what is in inventory and return whatevr you choose to equip
def open_inv_dict():
    print("You open your inventory and look a the contents")
    print("Your inventory contains...")
    print(','.join(inventory.keys()))
    print("Select item by typing name of item")
    selected = input("> ")
    in_hand = inventory[f'{selected}']
    equip_item(in_hand)
    

# fucntion that tells you what you equipped!
def equip_item(type):
    equip = input(f"Do you equip it or put the {type} away? \n>  ")

    if equip == "equip it":
        print(f"You equipped a {type}")
        return type
    elif equip == "put away":
        print(f"You put away {type}")
    else:
        print("Your are a bugger eatin moron, try again")
        equip_item(type)

def main(item):
    print(f"You come across a {item} !")

    action = input("what would you like to do? > ")
    
    if action == "pick up from list":
        inventory_list.append(item)
        open_inv_list()
    
    elif action == "pick up from dict":
        inventory[item_dict[0]] = item_dict[1]
        open_inv_dict()
        
    else:
        print("You do nothing")
        main(item, item_list)

main(item_list)
 

