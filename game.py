#Python3 game.py
from monsters import *
from sound import *
from gameparser import *
from player import *
from map import *
from mapfun import ascii_map


def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True
    
    
def print_room(room):         #print room name and description
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()


def print_inventory_items(items):         #print player's inventory
    if is_empty(inventory):
        print("----------------------------------")
        print()
        print("Your inventory is empty.")
        print()
    else:
        for item in items:
            print("----------------------------------")
            print()
            print("You have " + item['name'] + ".\n")
            
            
def print_equip_items(items):         #print player's inventory
    if items['weapon'] is None:
        print("Weapon: ")
    else:
        print('Weapon: ' + items['weapon']['name'])
    
    if items['armour'] is None:
        print ("Armour: ")
    else:
        print('Armour: ', items['armour']['name'])
    
    if is_empty(items['others']):
        print("Others:")
    else:
        for item in items['others']:
            print('Others: ', item['name'], '/n')
        
def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")
    
    
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]
    
    
def print_menu(exits, inv_items, equip_item):         #print list of commands
    print()
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
        
    for item in inv_items:
        items_id = item['id']
        items_name = item['name']
        print("OBSERVE " + items_id.upper() + " to look at your " + items_name + ".")
    
    for item in equip_item:
        items_id = item['id']
        items_name = item['name']
        print("EQUIP " + items_id.upper() + " to equip " + items_name + ".")
    print("VIEW MAP to look at the map")
    print("What do you want to do?")
    
        
def menu(exits, inv_items):         #calls print_menu() and normalises input()
    equip_items = []
    for item in inv_items:
        if item['equippable'] == True:
            equip_items.append(item)
            
    print_menu(exits, inv_items, equip_items)
    print()
    print("----------------------------------")
    user_input = input(">>")

    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def move(exits, direction):
    return rooms[exits[direction]]
        

def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"], direction) == True:
        current_room = move(current_room["exits"], direction)
        ###move_sound()
        print("----------------------------------")
        print_room(current_room)
        
    else:
        print("----------------------------------")
        print()
        print("You walked into a wall.\n")
        
        
def execute_observe(item_id):
    if item_id not in items:
        print("----------------------------------")
        print()
        print("You are dissapointed not to find that in your inventory.\n")
    else:
        item_id_name = items[item_id]
        if item_id_name not in inventory:
            print("----------------------------------")
            print()
            print("You are dissapointed not to find that in your inventory.\n")
        
        else:
            for item in inventory:
                if item == item_id_name:
                    print("----------------------------------")
                    print()
                    print(item_id_name['name'])
                    print(item_id_name['description'], '\n')
                    

        
        
def execute_equip(item_id):
    global equipped
    global inventory
    if item_id not in items:
        print("----------------------------------")
        print()
        print("You cannot equip that.\n")
        
    else:
        item_id_name = items[item_id]
        if item_id_name not in inventory:
            print("You cannot equip that\n.")
            return
        
        else:
            for item in inventory:
                if item == items[item_id]:
                    if items[item_id]['equippable'] == True:
                        if items[item_id]['weapon'] == True:
                            if equipped['weapon'] is None:
                                equipped['weapon'] = items[item_id]
                                inventory.remove(items[item_id])
                            else:
                                inventory.append(equipped['weapon'])
                                equipped['weapon'] = items[item_id]
                                inventory.remove(items[item_id])
                    
                
                
def execute_command(command, room):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("----------------------------------")
            print()
            print("Go where?\n")
            print("----------------------------------")

    elif command[0] == "observe":
        if len(command) > 1:
            execute_observe(command[1])
        else:
            print("----------------------------------")
            print()
            print("Look at what?\n")
            print("----------------------------------")
    
    elif command[0] == "view":
        if command[1] == "map":
            print("----------------------------------")
            print()
            print(ascii_map(room))
            print()
        else:
            print("----------------------------------")
            print()
            print("What?\n")
            print("----------------------------------")
    
    elif command[0] == "equip":
        if len(command) > 1:
            execute_equip(command[1])
        else:
            print("----------------------------------")
            print()
            print("Equip What?\n")
            print("----------------------------------")
    else:
        print("You are speaking nonsense.\n")
        
        
        
        
        

def main():
    play_sound()
    print(
 """    ____                                        ______                    __         
   / __ \__  ______  ____ ____  ____  ____     / ____/________ __      __/ /__  _____
  / / / / / / / __ \/ __ `/ _ \/ __ \/ __ \   / /   / ___/ __ `/ | /| / / / _ \/ ___/
 / /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /  / /___/ /  / /_/ /| |/ |/ / /  __/ /    
/_____/\__,_/_/ /_/\__, /\___/\____/_/ /_/   \____/_/   \__,_/ |__/|__/_/\___/_/     
                  /____/                                                             """)
    input("Press ENTER to continue.")
    print()
    print("----------------------------------")
    print_room(current_room)
    while True:
        print_inventory_items(inventory)
        
        print_equip_items(equipped)
        
        command = menu(current_room["exits"], inventory)
        
        execute_command(command, current_room)

if __name__ == "__main__":
    main()
