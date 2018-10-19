#Python3 player.py
from map import *
from items import *

current_room = start

inventory = [stick]

equipped = {'weapon' : None,
            'armour' : None,
            'others' : []
}