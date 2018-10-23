#Python3 player.py
from map import *
from items import *

current_room = start

inventory = [stick]

equipped = {'weapon' : None
}

inventory_heal = [potion]

player_hp = 20
max_player_hp = 20
player_level = 1
exp = 0
max_exp = player_level * 10

death = False