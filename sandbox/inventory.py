import random

master_item_dict = {
    "sword": {
        "Dmg": 10
    }, 
    "axe": {
        "Dmg": 11
    }, 
    "shield":{
        "Dmg": 3
    }, 
    "spear":{
        "Dmg": 9
    }, 
    "bucket of poop":{
        "Dmg": 100000
    },
    "stick":{
        "Dmg": 1
    }, 
    "cucumber":{
        "Dmg": 20
    },

}

inventory = ["stick", "cucumber"]

# function that adds item from game into the inventory dictionary
def add_inv(item, item_abr):
    inventory[f"{item_abr}"] = item

# fucntion open_inv to see what is in inventory and return whatevr you choose to equip
def open_inv_dict():
    print("You open your inventory and look a the contents")
    print("Your inventory contains...")
    print(inventory)
    print("Select item by typing name of item")
    selected = input("> ")
    equip_item(selected)
    

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

def main():
    print("You come across a chest !")

    action = input("what would you like to do? > ")

    random_item = random.choice(list(master_item_dict.keys()))
    
    if action == "open it":
        print(f"You open the chest and find {random_item}")
    elif action == "nothing":
        print("You move on and leave the chest")
    else:
        print("Type the right choice you moron!!")
        main()

    answer = input(f"Do you pick up the {random_item}?")
        
    if answer == "yes":
        inventory.append(random_item)
        open_inv_dict()
    elif answer == "no":
        print("You set it down and move on")
    else:
        print("Try again you dummy")
        main()
        
main()
 

