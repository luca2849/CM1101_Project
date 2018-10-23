#Python3 game.py
from monsters import *
from sound import *
from gameparser import *
from player import *
from map import *
from mapfun import ascii_map
from random_action import *
from items import *
from settings import *
from load_screen import load_screen
from threading import Timer
import os

#battle 
def room_event(room): # Function for deciding what happens when you enter a room
    if room['monster'] is not None:
        battle(room['monster'])
    elif room['boss'] is not None:
        battle_boss(room['boss'])
    if death:
        return
        
        
def print_battle(monster_gen): # Function for printing battle information
    print("-----------------------------------------------")
    print()
    print("A monster blocks your way.\n")
    print(monster_list[monster_gen].name, '\n')
    print(monster_list[monster_gen].ascii_art, '\n')
    print(monster_list[monster_gen].description, '\n')


def print_boss_battle(boss): # Function for printing boss battle information
    print("-----------------------------------------------")
    print()
    print("The boss appears in front of you.\n")
    print(boss.name, '\n')
    print(boss.description, '\n')
    

def display_monster_hp(monster_hp, full_monster_hp): # Function for displaying monster HP
    health = monster_hp
    max_health = full_monster_hp  
    health_dashes = 20
    
    dash_convert = max_health/health_dashes
    current_dashes = int(health/dash_convert)
    remaining_health = health_dashes - current_dashes
    
    health_display = ''.join(['-' for i in range(current_dashes)])
    remaining_display = ''.join([' ' for i in range(remaining_health)])
    print("HP: ""|" + health_display + remaining_display + "|", health, "/", max_health)


def display_player_hp(player_hp, full_player_hp): # Function for displaying player HP
    health = player_hp
    max_health = full_player_hp
    health_dashes = 20
    
    dash_convert = max_health/health_dashes
    current_dashes = int(health/dash_convert)
    remaining_health = health_dashes - current_dashes
    
    health_display = ''.join(['-' for i in range(current_dashes)])
    remaining_display = ''.join([' ' for i in range(remaining_health)])
    print("HP: ""|" + health_display + remaining_display + "|", health, "/", max_health)
    

def print_battle_menu(): # Function to print all of the options available to the player
    print("You can:")
    if show_attack:
        print("ATTACK to attack monster")
    if show_potions:
        if potion['amount'] > 0:
            print("USE POTION to use potion")
    

def is_battle(monster_hp): # Function for checking if a battle can continue by checking if the monster is still alive
    if monster_hp > 0:
        return True
    
    
def battle_seq(monster_gen, monster_hp, full_monster_hp): # Function to print the battle sequence
    global exp
    global player_hp
    global max_player_hp
    global death
    
    
    while is_battle(monster_hp):
        if monster_hp > 0:
            print("-----------------------------------------------")
            print()
            print(monster_list[monster_gen].name)
            display_monster_hp(monster_hp, full_monster_hp)
            print("You:")
            display_player_hp(player_hp, max_player_hp)
            print()
            print_battle_menu()
            print()
            print("-----------------------------------------------")
            
            player_input = input(">>")
            normalised_player_input = normalise_input(player_input)
            os.system('cls')
            
            if 0 == len(normalised_player_input):
                 continue

            if normalised_player_input[0] == "attack":
                player_atk = random_atk(player_level, equipped['weapon'])
                monster_hp -= player_atk
                print("-----------------------------------------------")
                print()
                print("You deal", player_atk, "damage.")
                if monster_hp > 0:
                    monster_atk = random_monster_atk(monster_gen)
                    player_hp -= monster_atk
                    print(monster_list[monster_gen].name,"deals", monster_atk, "to you.")
                    print()
                    #if player_hp <= 0:
                        #death = True
                        #return
            elif normalised_player_input[0] == 'use':
                if normalised_player_input[1] == 'potion':
                    execute_use(normalised_player_input[1])
                else:
                    print("-----------------------------------------------")
                    print()
                    print("Use what?\n")
                    print("-----------------------------------------------")
                
            else:
                print("Do what?\n")
    exp_gain = int(random.uniform(monster_list[monster_gen].tier * 3, monster_list[monster_gen].tier * 5))
    exp += exp_gain
    print()
    print("You defeated", monster_list[monster_gen].name)
    print("You gain", exp_gain, "exp.")
    print()
    print_if_level_up()
    after_battle(monster_gen)
    print("-----------------------------------------------")
    

def after_battle(monster_gen): # Function for the after-battle sequence
    global dropped_items
    append_item = True
    item = random_drop(monster_gen)
    drop = monster_list[monster_gen].drops[item]
    if drop in inventory:
        append_item = False
    elif equipped['weapon'] is None:
        append_item = True
    elif drop == equipped['weapon']:
        append_item = False
    if append_item:
        dropped_items.append(drop)
        print(monster_list[monster_gen].name, 'dropped', drop['name'])
    print()
    

def after_battle_boss(boss): # Function to drop bosses items
    global dropped_items
    for item in boss.drops:
        drop = item
    dropped_items.append(drop)
    print(boss.name, 'dropped', drop['name'])
    print()
    
    
def print_if_level_up(): # Function to check if the player has levelled up and if so to display a congratulatory message
    global exp
    global player_level
    
    if exp >= max_exp:
        print("LEVEL UP    (hp +10, max hp +20, attack +3)")
        
    
def boss_battle_seq(boss, boss_hp, max_boss_hp): # Function to print the boss battle sequence
    global exp
    global player_hp
    global max_player_hp
    global death
    
    
    while is_battle(boss_hp):
        if boss_hp > 0:
            print("-----------------------------------------------")
            print()
            print(boss.name)
            display_monster_hp(boss_hp, max_boss_hp)
            print("You:")
            display_player_hp(player_hp, max_player_hp)
            print()
            print_battle_menu()
            print()
            print("-----------------------------------------------")
            
            player_input = input(">>")
            normalised_player_input = normalise_input(player_input)
            os.system('cls')
            
            if 0 == len(normalised_player_input):
                 continue

            if normalised_player_input[0] == "attack":
                player_atk = random_atk(player_level, equipped['weapon'])
                boss_hp -= player_atk
                print("-----------------------------------------------")
                print()
                print("You deal", player_atk, "damage.")
                if boss_hp > 0:
                    boss_atk = random_boss_atk(boss)
                    player_hp -= boss_atk
                    print(boss.name,"deals", boss_atk, "to you.")
                    print()
                    if player_hp <= 0:
                        death = True
                        return
                    
            elif normalised_player_input[0] == 'use':
                
                if normalised_player_input[1] == 'potion':
                    execute_use(normalised_player_input[1])
                else:
                    print("-----------------------------------------------")
                    print()
                    print("Use what?\n")
                    print("-----------------------------------------------")
            else:
                print("Do what?\n")
                
    exp_gain = int(random.uniform(boss.tier * 3, boss.tier * 5))
    exp += exp_gain
    print()
    print("You defeated", boss.name)
    print("You gain", exp_gain, "exp.")
    print()
    print_if_level_up()
    after_battle_boss(boss)
    print("-----------------------------------------------")

    
    
def battle_boss(boss): # Function to start the boss battle
    print_boss_battle(boss)
    boss_battle_seq(boss, boss_hp, max_boss_hp)
    if death:
        return
    
def battle(monster_number): # Function to decided what monster to spawn dependent on the room and tier
    x = 0
    y = 1
    if monster_number == 1:
        x = 0
        y = 4
    elif monster_number == 2:
        x = 4
        y = 8
    elif monster_number == 3:
        x = 8
        y = 12
        
    monster_gen = random_monster(x,y)
    print_battle(monster_gen)
    monster_hp = random_stats(monster_gen)
    full_monster_hp = monster_hp
    battle_seq(monster_gen, monster_hp, full_monster_hp)
    if death:
        return


#others  
def game_over():
    print()
    
def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True
    
 #room and menu   
def print_room(room):         #print room name and description
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()


def print_inventory_items(items):         #print player's inventory
    if potion['amount'] <= 0:
        if is_empty(inventory):
            print("-----------------------------------------------")
            print()
            print("Your inventory is empty.")
            print()
    else:
        item_list = []
        for item in items:
            item_list.append(item['name'])
        if potion['amount']>0:
            potion_amount = str(potion['amount'])
            item_list.append(potion['name'] + 's: ' + potion_amount)
        item_str = ', '.join(item_list)
        print("-----------------------------------------------")
        print()
        print("You have " + item_str + ".\n")
            
            
def print_equip_items(items):         #print player's inventory
    print('Equipments:')
    if items['weapon'] is None:
        print("Weapon: ")
    else:
        print('Weapon: ' + items['weapon']['name'] + '(+',items['weapon']['power'] * 3,'atk)')
        
def print_exit(direction, leads_to): # Function to print all possible exits
    print("GO " + direction.upper() + " to " + leads_to + ".")
    
    
def exit_leads_to(exits, direction): # Function to show where an exit leads
    return rooms[exits[direction]]["name"]
    
    
def print_menu(exits, inv_items, equip_item, dropped_items):         #print list of commands  
    print()
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    
    if show_potions:
        if potion['amount'] > 0:
            print("USE POTION to use potion")
        
    if show_observe:
        for item in inv_items:
            items_id = item['id']
            items_name = item['name']
            print("OBSERVE " + items_id.upper() + " to look at your " + items_name + ".")
    
    if show_observe:
        if potion['amount'] > 0:
            print("OBSERVE POTION to look at your potion.")
    
    if show_equip:
        for item in equip_item:
            items_id = item['id']
            items_name = item['name']
            print("EQUIP " + items_id.upper() + " to equip " + items_name + ".")
        
    if show_obtain:
        for item in dropped_items:
            items_id = item['id']
            items_name = item['name']
            print("OBTAIN " + items_id.upper() + " to obtain " + items_name + ".")
     
    if show_drop:
        for item in inv_items:
            items_id = item['id']
            items_name = item['name']
            print("DROP " + items_id.upper() + " to drop " + items_name + ".")
    
    if show_map:
        print("VIEW MAP to look at the map")
    
    print("SETTINGS to change settings")
    print("What do you want to do?")
    
        
def menu(exits, inv_items):         #calls print_menu() and normalises input()
    equip_items = []
    for item in inv_items:
        if item['equippable']:
            equip_items.append(item)
            
    print_menu(exits, inv_items, equip_items, dropped_items)
    print()
    print("-----------------------------------------------")
    user_input = input(">>")

    normalised_user_input = normalise_input(user_input)

    os.system('cls')

    return normalised_user_input


def is_valid_exit(exits, chosen_exit): # Function to check if a given exit is valid
    return chosen_exit in exits


def move(exits, direction): # Function to move the player to a new room
    return rooms[exits[direction]]
        

def check_key(): # Function checks if the player has the boss room key
    for item in inventory:
        if item['id'] == 'key':
            return True
    return False
            
            
def execute_go(direction): # Function to move the player
    global current_room
    global dropped_items
    global death
    
    if is_valid_exit(current_room["exits"], direction):
        if move(current_room["exits"], direction) == boss:
            if check_key():
                current_room = move(current_room["exits"], direction)
            else:
                print("The gate is locked, you require a key.")
                return
        else:
            current_room = move(current_room["exits"], direction)
        dropped_items = []
        if current_room['item'] is not None:
            if current_room['item'] == key:
                if check_key() == False:
                    dropped_items.append(current_room['item'])
            if current_room['item'] == potion:
                dropped_items.append(current_room['item'])
        ###move_sound()
        room_event(current_room)
        print_room(current_room)
        if current_room['trap']:
            death = True
            return
        
    else:
        print("-----------------------------------------------")
        print()
        print("You walked into a wall.\n")
        
    if death:
        return
        
        
def execute_observe(item_id): # Function to process the observe command to see more information about an item
    if item_id not in items:
        print("-----------------------------------------------")
        print()
        print("You are dissapointed not to find that in your inventory.\n")
    elif item_id == 'potion':
        print("-----------------------------------------------")
        print()
        print(potion['description'])
        print()
    else:
        item_id_name = items[item_id]
        if item_id_name not in inventory:
            print("-----------------------------------------------")
            print()
            print("You are dissapointed not to find that in your inventory.\n")
        
        else:
            for item in inventory:
                if item == item_id_name:
                    print("-----------------------------------------------")
                    print()
                    if item_id_name['type'] == 'weapon':
                        print(item_id_name['name'], "(+", item_id_name['power'] * 3, "Attack)")
                    else:
                        print(item_id_name['name'])
                    print(item_id_name['description'], '\n')
                    

        
        
def execute_equip(item_id): # Function to equip a given item
    global equipped
    global inventory
    if item_id not in items:
        print("-----------------------------------------------")
        print()
        print("You cannot equip that.\n")
        
    else:
        item_id_name = items[item_id]
        if item_id_name not in inventory:
            print("-----------------------------------------------")
            print()
            print("You cannot equip that.\n")
            return
        
        else:
            for item in inventory:
                if item == items[item_id]:
                    if items[item_id]['equippable']:
                        if items[item_id]['type'] == 'weapon':
                            if equipped['weapon'] is None:
                                equipped['weapon'] = items[item_id]
                                inventory.remove(items[item_id])
                            else:
                                inventory.append(equipped['weapon'])
                                equipped['weapon'] = items[item_id]
                                inventory.remove(items[item_id])
                                
                    
                 
def execute_obtain(item_id): # Function to allow players to pick up an item from the ground
    global inventory
    global dropped_items
    global potion
    
    if item_id not in items:
        print("-----------------------------------------------")
        print()
        print("You cannot obtain that.\n")
        
    else:
        item_id_name = items[item_id]
        if item_id_name not in dropped_items:
            print("-----------------------------------------------")
            print()
            print("You cannot obtain that.\n")
            return
        elif item_id_name == potion:
            for item in dropped_items:
                if item == items[item_id]:
                    potion['amount'] += 1
                    dropped_items.remove(items[item_id])
        else:
            for item in dropped_items:
                if item == items[item_id]:
                    inventory.append(items[item_id])
                    dropped_items.remove(items[item_id])
                    

def execute_drop(item_id): # Function to let players drop items
    global inventory
    global dropped_items
    if item_id not in items:
        print("-----------------------------------------------")
        print()
        print("You cannot drop that.\n")
        
    else:
        item_id_name = items[item_id]
        if item_id_name not in inventory:
            print("-----------------------------------------------")
            print()
            print("You cannot drop that.\n")
            return
        
        else:
            for item in inventory:
                if item == items[item_id]:
                    dropped_items.append(items[item_id])
                    inventory.remove(items[item_id])


def execute_use(item_id): # Function to letthe player use potions to heal
    global potion
    global player_hp
    
    if item_id not in items:
        print("-----------------------------------------------")
        print()
        print("You cannot use that.\n")
        print()
        
    else:
        potion_amount = potion['amount']
        if potion_amount > 0:
            print("-----------------------------------------------")
            print()
            if player_hp < max_player_hp:
                potion_amount -= 1
                potion['amount'] = potion_amount
                player_hp += max_player_hp // 4
                restored_health = max_player_hp // 4
                if player_hp > max_player_hp:
                    restored_health -= max_player_hp - player_hp
                    player_hp = max_player_hp
                print("You restored " + str(restored_health) + " health.\n")
            else:
                print("You are already at full health.")
            print()
        else:
            print("You don't have any potions left.")
                    
                

                    
            
<<<<<<< HEAD
def execute_command(command, room): # Function to process general commands and route them to their functions
    if 0 == len(command):
=======
def execute_command(command, room):
    if len(command) == 0:
>>>>>>> d390105f766f72eff4752e6cb7058c71fe3ee443
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
            if death:
                return
        else:
            print("-----------------------------------------------")
            print()
            print("Go where?\n")

    elif command[0] == "observe":
        if len(command) > 1:
            execute_observe(command[1])
        else:
            print("-----------------------------------------------")
            print()
            print("Look at what?\n")
    
    elif command[0] == "view":
        print("-----------------------------------------------")
        print()
        if len(command) > 1 and command[1] == "map":
            print(ascii_map(room))
            print()
        else:
            print("View what?\n")
    
    elif command[0] == 'equip':
        if len(command) > 1:
            execute_equip(command[1])
        else:
            print("-----------------------------------------------")
            print()
            print("Equip What?\n")
            
    elif command[0] == 'drop':
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("-----------------------------------------------")
            print()
            print("Equip What?\n")
    
    elif command[0] == 'obtain':
        if len(command) > 1:
            execute_obtain(command[1])
        else:
            print("-----------------------------------------------")
            print()
            print("Obtain what?\n")
            
    elif command[0] == 'use':
        if len(command) > 1 and command[1] == 'potion':
            execute_use(command[1])
        else:
            print("-----------------------------------------------")
            print()
            print("Use what?\n")
    
    elif command[0] == 'settings':
        settings()
            
    else:
        print("-----------------------------------------------")
        print()
        print("You are speaking nonsense.\n")
        
def display_exp(exp, max_exp): # Function to display current experience
    dashes = 20
    
    dash_convert = max_exp/dashes
    current_dashes = int(exp/dash_convert)
    remaining_exp = dashes - current_dashes
    
    exp_display = ''.join(['-' for i in range(current_dashes)])
    remaining_display = ''.join([' ' for i in range(remaining_exp)])
    print("EXP: ""|" + exp_display + remaining_display + "|", exp, "/", max_exp)        
        
    
def level_up():
    global exp
    global player_level
    global player_hp
    global max_player_hp
    global max_exp
    
    while exp >= max_exp:
        max_exp = player_level * 10
        exp -= max_exp
        player_level += 1
        player_hp += 10
        max_player_hp += 20
        level_up()
        max_exp = player_level * 10
        
        
def game_over():
    print("-----------------------------------------------")
    print()
    print("Gameover \nYou lose")
    game_over_sound()
    input("Press ENTER to continue.")
    
    
#settings
def print_setting_menu():
    #music
    print("-----------------------------------------------")
    if music:
        print('MUSIC: On')
    else:
        print('MUSIC: Off')
    print("-----------------------------------------------")
    
    #help
    if show_help:
        print('Show HELP : On')
    else:
        print('Show HELP : Off')
    
    #help individual
    if show_attack:
        print('    Show ATTACK help : On')
    else:
        print('    Show ATTACK help : Off')

    if show_potions:
        print('    Show POTION help : On')
    else:
        print('    Show POTION help : Off')
        
    if show_observe:
        print('    Show OBSERVE help : On')
    else:
        print('    Show OBSERVE help : Off')
    
    if show_equip:
        print('    Show EQUIP help : On')
    else:
        print('    Show EQUIP help : Off')

    if show_obtain:
        print('    Show OBTAIN help : On')
    else:
        print('    Show OBTAIN help : Off')
        
    if show_drop:
        print('    Show DROP help : On')
    else:
        print('    Show DROP help : Off')

    if show_map:
        print('    Show MAP help : On')
    else:
        print('    Show MAP help : Off')
        
    print("-----------------------------------------------")
    print("SETTING HELP for help")
    print()
    print("Quit to apply settings")
    print("-----------------------------------------------")
    
    
def settings_action(command): # Function to process settings, show players a help menu and allow for settings to be changed
    global music
    global show_help
    global show_attack
    global show_potions
    global show_observe
    global show_equip
    global show_obtain
    global show_drop
    global show_map
    global setting
    
    if 0 == len(command):
        return

    if command[0] == "setting":
        if len(command) > 1:
            if command[1] == "help":
                print("-----------------------------------------------")
                print()
                print("MUSIC to toggle Music on or off, HELP to toggle Help on or off...")
            else:
                print("That is not a valid input.")
        else:
            print("That is not a valid input.")
            
    elif command[0] == "music":
        if music:
            music = False
        else:
            music = True

    elif command[0] == "help":
        if show_help == True:
            show_help = False
            show_attack = False
            show_potions = False
            show_observe = False
            show_equip = False
            show_obtain = False
            show_drop = False
            show_map = False
        elif show_help == False:
            show_help = True
            show_attack = True
            show_potions = True
            show_observe = True
            show_equip = True
            show_obtain = True
            show_drop = True
            show_map = True
            
    elif command[0] == "attack":
        if show_attack:
            show_attack = False
        else:
            show_attack = True

    elif command[0] == "potion":
        if show_potions:
            show_potions = False
        else:
            show_potions = True

    elif command[0] == "observe":
        if show_observe:
            show_observe = False
        else:
            show_observe = True

    elif command[0] == "equip":
        if show_equip:
            show_equip = False
        else:
            show_equip = True

    elif command[0] == "obtain":
        if show_obtain:
            show_obtain = False
        else:
            show_obtain = True

    elif command[0] == "drop":
        if show_drop:
            show_drop = False
        else:
            show_drop = True
            
    elif command[0] == "map":
        if show_map:
            show_map = False
        else:
            show_map = True
    
    elif command[0] == "quit":
        setting = False
        os.system('cls')

    
def settings(): # Function to print the settings menu
    global setting
    
    setting = True

    os.system('cls')
    
    while setting:
        print_setting_menu()
    
        user_input = input(">>")

        settings_action(normalise_input(user_input))

        os.system('cls')


def print_class_menu(): # Function to print a menu to show the user class choices
    print("-----------------------------------------------")
    print("Choose a class:")
    print("ALCHEMIST: Start with 3 potions.")
    print("WARRIOR: Start at level 2.")
    print("MAGE: Start with 5 exp and 2 potions.")
    print("-----------------------------------------------")
    
    
def class_action(command): # Function to apply class bonuses
    global potion
    global exp
    global is_choose_class
    global class_choice

    if 0 == len(command):
        return
            
    elif command[0] == 'alchemist':
        potion['amount'] = 3
        class_choice = 'Alchemist'

    elif command[0] == 'warrior':
        exp += 10
        class_choice = 'Warrior'

    elif command[0] == 'mage':
        exp += 5
        potion['amount'] = 2
        class_choice = 'Mage'
    
    else:
        return

    
def choose_class(): # Function to get the players class choice
    global choose_class
    
    is_choose_class = True
    
    while is_choose_class:
        print_class_menu()
    
        user_input = input(">>")

        class_action(normalise_input(user_input))

        os.system('cls')

        if class_choice != '':
            is_choose_class = False    
        
        
<<<<<<< HEAD
def main(): # Function for the main game loop
    play_sound()
=======
def main():
>>>>>>> d390105f766f72eff4752e6cb7058c71fe3ee443
    print(
 """    ____                                        ______                    __         
   / __ \__  ______  ____ ____  ____  ____     / ____/________ __      __/ /__  _____
  / / / / / / / __ \/ __ `/ _ \/ __ \/ __ \   / /   / ___/ __ `/ | /| / / / _ \/ ___/
 / /_/ / /_/ / / / / /_/ /  __/ /_/ / / / /  / /___/ /  / /_/ /| |/ |/ / /  __/ /    
/_____/\__,_/_/ /_/\__, /\___/\____/_/ /_/   \____/_/   \__,_/ |__/|__/_/\___/_/     
                  /____/                                                             """)
    input("Press ENTER to continue.")
    load_screen()
    play_sound()
    is_choose_class = False
    choose_class()
    print("-----------------------------------------------")
    print_room(current_room)
    level_up()
    global player_hp
    player_hp = int(max_player_hp)
    while True:
        #music settings
        if music:
            play_sound()
        else:
            stop_sound()
        
        #win condition
        for item in inventory:
            if item == trophy_for_winning_the_game:
                print("-----------------------------------------------")
                print()
                print("You've completed the game!")
                input("Press ENTER to continue.")
                return
        
        #check level up conditions
        level_up()
        
        #main game
        print_inventory_items(inventory)
        
        print_equip_items(equipped)
        print()
        print("Player:", '('+class_choice+')')
        display_player_hp(player_hp, max_player_hp)
        print("Your level:", player_level)
        display_exp(exp, max_exp)
        
        command = menu(current_room["exits"], inventory)
        
        execute_command(command, current_room)
        
        #game over
        if death:
            game_over()
            break

if __name__ == "__main__":
    main()
