#Python3 game.py
from monsters import *
from sound import *
from gameparser import *
from player import *
from map import *
from mapfun import ascii_map
from random_action import *

#battle
def room_event(room):
    if room['monster'] is not None:
        battle(room['monster'])
    elif room['boss'] is not None:
        battle_boss(room['boss'])
    if death == True:
        return
        
        
def print_battle(monster_gen):  
    print("----------------------------------")
    print()
    print("A monster blocks your way.\n")
    print(monster_list[monster_gen].name, '\n')
    print(monster_list[monster_gen].description, '\n')


def print_boss_battle(boss):
    print("----------------------------------")
    print()
    print("The boss appears in front of you.\n")
    print(boss.name, '\n')
    print(boss.description, '\n')
    

def display_monster_hp(monster_hp, full_monster_hp):
    health = monster_hp
    max_health = full_monster_hp  
    health_dashes = 20
    
    dash_convert = max_health/health_dashes
    current_dashes = int(health/dash_convert)
    remaining_health = health_dashes - current_dashes
    
    health_display = ''.join(['-' for i in range(current_dashes)])
    remaining_display = ''.join([' ' for i in range(remaining_health)])
    print("HP: ""|" + health_display + remaining_display + "|", health, "/", max_health)


def display_player_hp(player_hp, full_player_hp):
    health = player_hp
    max_health = full_player_hp
    health_dashes = 20
    
    dash_convert = max_health/health_dashes
    current_dashes = int(health/dash_convert)
    remaining_health = health_dashes - current_dashes
    
    health_display = ''.join(['-' for i in range(current_dashes)])
    remaining_display = ''.join([' ' for i in range(remaining_health)])
    print("HP: ""|" + health_display + remaining_display + "|", health, "/", max_health)
    

def print_battle_menu():
    print("You can:")
    print("ATTACK to attack monster")
    

def is_battle(monster_hp):
    if monster_hp > 0:
        return True
    
    
def battle_seq(monster_gen, monster_hp, full_monster_hp):
    global exp
    global player_hp
    global max_player_hp
    global death
    
    
    while is_battle(monster_hp):
        if monster_hp > 0:
            print("----------------------------------")
            print()
            print(monster_list[monster_gen].name)
            display_monster_hp(monster_hp, full_monster_hp)
            print("You:")
            display_player_hp(player_hp, max_player_hp)
            print()
            print_battle_menu()
            print()
            print("----------------------------------")
            
            player_input = input(">>")
            normalised_player_input = normalise_input(player_input)
            
            if 0 == len(normalised_player_input):
                 continue

            if normalised_player_input[0] == "attack":
                player_atk = random_atk(player_level, equipped['weapon'])
                monster_hp -= player_atk
                print("----------------------------------")
                print()
                print("You deal", player_atk, "damage.")
                if monster_hp > 0:
                    monster_atk = random_monster_atk(monster_gen)
                    player_hp -= monster_atk
                    print(monster_list[monster_gen].name,"deals", monster_atk, "to you.\n")
                    if player_hp <= 0:
                        death = True
                        return
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
    

def after_battle(monster_gen):
    global dropped_items
    item = random_drop(monster_gen)
    drop = monster_list[monster_gen].drops[item]
    dropped_items.append(drop)
    print(monster_list[monster_gen].name, 'dropped', drop['name'])
    print()
    

def after_battle_boss(boss):
    global dropped_items
    for item in boss.drops:
        drop = item
        print(drop)
    dropped_items.append(drop)
    print("----------------------------------")
    print()
    print(boss.name, 'dropped', drop['name'])
    print()
    
    
def print_if_level_up():
    global exp
    global player_level
    
    if exp >= max_exp:
        print("LEVEL UP    (hp +10, max hp +20, attack +3)")
        
    
def boss_battle_seq(boss, boss_hp, max_boss_hp):
    global exp
    global player_hp
    global max_player_hp
    global death
    
    
    while is_battle(boss_hp):
        if boss_hp > 0:
            print("----------------------------------")
            print()
            print(boss.name)
            display_monster_hp(boss_hp, max_boss_hp)
            print("You:")
            display_player_hp(player_hp, max_player_hp)
            print()
            print_battle_menu()
            print()
            print("----------------------------------")
            
            player_input = input(">>")
            normalised_player_input = normalise_input(player_input)
            
            if 0 == len(normalised_player_input):
                 continue

            if normalised_player_input[0] == "attack":
                player_atk = random_atk(player_level, equipped['weapon'])
                boss_hp -= player_atk
                print("You deal", player_atk, "damage.")
                if boss_hp > 0:
                    boss_atk = random_boss_atk(boss)
                    player_hp -= boss_atk
                    print(boss.name,"deals", boss_atk, "to you.")
                    if player_hp <= 0:
                        death = True
                        return
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
    
    
def battle_boss(boss):
    print_boss_battle(boss)
    boss_battle_seq(boss, boss_hp, max_boss_hp)
    if death == True:
        return
    
def battle(monster_number):
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
    if death == True:
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
    if is_empty(inventory):
        print("----------------------------------")
        print()
        print("Your inventory is empty.")
        print()
    else:
        item_list = []
        for item in items:
            item_list.append(item['name'])
        item_str = ', '.join(item_list)
        print("----------------------------------")
        print()
        print("You have " + item_str + ".\n")
            
            
def print_equip_items(items):         #print player's inventory
    print('Equipments:')
    if items['weapon'] is None:
        print("Weapon: ")
    else:
        print('Weapon: ' + items['weapon']['name'] + '(+',items['weapon']['power'] * 3,'atk)')
    
    if items['armour'] is None:
        print ("Armour: ")
    else:
        print('Armour: ', items['armour']['name'])
        
def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")
    
    
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]
    
    
def print_menu(exits, inv_items, equip_item, dropped_items):         #print list of commands
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
        
    for item in dropped_items:
        items_id = item['id']
        items_name = item['name']
        print("OBTAIN " + items_id.upper() + " to equip " + items_name + ".")
    print("VIEW MAP to look at the map")
    print("What do you want to do?")
    
        
def menu(exits, inv_items):         #calls print_menu() and normalises input()
    equip_items = []
    for item in inv_items:
        if item['equippable'] == True:
            equip_items.append(item)
            
    print_menu(exits, inv_items, equip_items, dropped_items)
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
    global dropped_items
    if is_valid_exit(current_room["exits"], direction) == True:
        current_room = move(current_room["exits"], direction)
        dropped_items = []
        ###move_sound()
        print("----------------------------------")
        print_room(current_room)
        room_event(current_room)
        
    else:
        print("----------------------------------")
        print()
        print("You walked into a wall.\n")

    if death == True:
        return
        
        
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
                    if item_id_name['type'] == 'weapon':
                        print(item_id_name['name'], "(+", item_id_name['power']*3, "Attack)")
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
            print("You cannot equip that.\n")
            return
        
        else:
            for item in inventory:
                if item == items[item_id]:
                    if items[item_id]['equippable'] == True:
                        if items[item_id]['type'] == 'weapon':
                            if equipped['weapon'] is None:
                                equipped['weapon'] = items[item_id]
                                inventory.remove(items[item_id])
                                print("----------------------------------")
                                print()
                                print("You equipped " + items[item_id]['name'] +'.')
                            else:
                                inventory.append(equipped['weapon'])
                                equipped['weapon'] = items[item_id]
                                inventory.remove(items[item_id])
                                print("----------------------------------")
                                print()
                                print("You equipped" + items[item_id]['name'] +'.')
                                
                        elif items[item_id]['type'] == 'armour':
                            if equipped['armour'] is None:
                                equipped['armour'] = items[item_id]
                                inventory.remove(items[item_id])
                                print("----------------------------------")
                                print()
                                print("You equipped" + items[item_id]['name'] +'.')
                            else:
                                inventory.append(equipped['armour'])
                                equipped['armour'] = items[item_id]
                                inventory.remove(items[item_id])
                                print("----------------------------------")
                                print()
                                print("You equipped" + items[item_id]['name'] +'.')
                    
                 
def execute_obtain(item_id):
    global inventory
    global dropped_items
    if item_id not in items:
        print("----------------------------------")
        print()
        print("You cannot obtain that.\n")
        
    else:
        item_id_name = items[item_id]
        if item_id_name not in dropped_items:
            print("----------------------------------")
            print()
            print("You cannot obtain that.\n")
            return
        
        else:
            for item in dropped_items:
                if item == items[item_id]:
                    inventory.append(items[item_id])
                    dropped_items.remove(items[item_id])

                
def execute_command(command, room):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
            if death == True:
                return
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
    
    elif command[0] == 'equip':
        if len(command) > 1:
            execute_equip(command[1])
        else:
            print("----------------------------------")
            print()
            print("Equip What?\n")
            print("----------------------------------")
    
    elif command[0] == 'obtain':
        if len(command) > 1:
            execute_obtain(command[1])
        else:
            print("----------------------------------")
            print()
            print("Obtain what?\n")
            print("----------------------------------")
            
    else:
        print("You are speaking nonsense.\n")
        
        
def display_exp(exp, max_exp):
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
    print("----------------------------------")
    print()
    print("Gameover \nYou lose")
    game_over_sound()
    input("Press ENTER to continue.")
    
    
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
        for item in inventory:
            if item == trophy_for_winning_the_game:
                print("----------------------------------")
                print()
                print("You defeated the game!")
                input("Press ENTER to continue.")
                return
            
        level_up()
        
        print_inventory_items(inventory)
        
        print_equip_items(equipped)
        print()
        print("Player:")
        display_player_hp(player_hp, max_player_hp)
        print("Your level:", player_level)
        display_exp(exp, max_exp)
        
        command = menu(current_room["exits"], inventory)
        
        execute_command(command, current_room)
        
        if death == True:
            game_over()
            break

if __name__ == "__main__":
    main()
