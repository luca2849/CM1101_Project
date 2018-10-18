#Python3 game.py
from monsters import *
from sound import *
from gameparser import *
from player import *
from map import *
from mapfun import ascii_map

def print_room(room):         #print room name and description
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()


def print_inventory_items(items):         #print player's inventory
    for item in items:
        if items == "":
            return None
        else:
            print("----------------------------------")
            print()
            print("You have " + items +".\n")
     
        
def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")
    
    
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]
    
    
def print_menu(exits, inv_items):         #print list of commands
    print()
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
        
    for item in inv_items:
        items_id = item["id"]
        items_name = item["name"]
        print("OBSERVE " + items_id.upper() + " to look at your " + items_name + ".")
    
    print("VIEW MAP to look at the map")
    print("What do you want to do?")
    
        
def menu(exits, inv_items):         #calls print_menu() and normalises input()
    print_menu(exits, inv_items)
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
        print("----------------------------------")
        
        
def execute_observe(item_id):
    if item_id not in items:
        print("----------------------------------")
        print()
        print("You are disappointed not to find that in your inventory.\n")
        print("----------------------------------")
    else:
        item_id_name = items[item_id]
        if item_id_name not in inventory:
            print("----------------------------------")
            print()
            print("You are disappointed not to find that in your inventory.\n")
            print("----------------------------------")
            return
        
        else:
            for item in inventory:
                if item == item_id_name:
                    print("----------------------------------")
                    print()
                    print(item_id_name["description"], '\n')
        
        
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
            print("----------------------------------")
        else:
            print("----------------------------------")
            print()
            print("What?\n")
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
        
        command = menu(current_room["exits"], inventory)
        
        execute_command(command, current_room)

if __name__ == "__main__":
    main()
