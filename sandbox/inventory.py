#created dictionary called inventory
inventory = {"stick": "stick", "cucumber": "cucumber"}
inventory_lst = ["stick", "cucumber"]

# function that adds item from game into the inventory dictionary
def add_inv(item, item_abr):
    inventory[f"{item_abr}"] = item

# fucntion open_inv to see what is in inventory and return whatevr you choose to equip
def open_inv_list():
    print("You open your inventory and look a the contents")
    print("Your inventory contains...")
    print(','.join(inventory_lst))
    print("Select item by typing number of item")
    selected = input("> ")
    in_hand = inventory_lst[(int(selected))]
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

def main():
    print("You come across a sword! Do you pick it up?")

    action = input("what would you like to do? > ")
    
    if action == "pick up from list":
        open_inv_list()
    
    elif action == "pick up from dict":
        open_inv_dict()
        
    else:
        print("You do nothing")
        main()

main()
 

