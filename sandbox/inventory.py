import random

master_item_list = ["sword", "axe", "shield", "spear", "bucket of poop"]
master_item_dict = {"sword": "sword", "axe": "axe", "shield": "sheild", "spear": "spear", "bucket of poop": "bucket of poop"}
inventory = {"stick": "stick", "cucumber": "cucumber"}
inventory_list = ["stick", "cucumber"]

item_list = random.choice(tuple(master_item_list))
item_dict = random.choice(list(master_item_dict.items()))
item_dict_single = item_dict[1]



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

def main(item_list, item_dict, item_dict_single):
    print("You come across a chest !")

    action = input("what would you like to do? > ")
    
    if action == "open up from list":
        print(f"It is a {item_list}")
        answer = input(f"Do you pick up the {item_list}?")
        
        if answer == "yes":
            inventory_list.append(item_list)
            open_inv_list()
        elif answer == "no":
            print("You set it down and move on")
        else:
            print("Try again you dummy")
            main(item_list, item_dict, item_dict_single)
    
    elif action == "open up from dict":
        print(f"It is a {item_dict_single}")
        answer = input(f"Do you pick up the {item_dict_single}?")
        
        if answer == "yes":
            inventory[item_dict[0]] = item_dict[1]
            open_inv_dict()
        elif answer == "no":
            print("You set it down and move on")
        else:
            print("Try again you dummy")
            main(item_list, item_dict, item_dict_single)
        
    else:
        print("You do nothing")
        main(item_list, item_dict, item_dict_single)

main(item_list, item_dict, item_dict_single)
 

