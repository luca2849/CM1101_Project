#python3 map.py
from monsters import *
from items import *

r1 = {
    'name' : 'room 1',
    'position' : 'position1',
    'description' :"""There's a potion in the room.""",
    'exits' : {'north' : 'rm5'},
    'monster' : 1,
    'boss' : None,
    'item' : potion,
    'trap' : False
}

r2 = {
    'name' : 'room 2',
    'position' : 'position2',
    'description' :"""There's a potion in the room.""",
    'exits' : {'north' : 'rm6', 'east' : 'rm3', 'west' : 'rm1'},
    'monster' : 1,
    'boss' : None,
    'item' : potion,
    'trap' : False
}

r3 = {
    'name' : 'room 3',
    'position' : 'position3',
    'description' :"""It's a trap! The floor drops beneath you.""",
    'exits' : {},
    'monster' : None,
    'boss' : None,
    'item' : None,
    'trap' : True
}

r4 = {
    'name' : 'room 4',
    'position' : 'position4',
    'description' :"""No monsters in this room, you see something shining in the corner.""",
    'exits' : {'east': 'rm5'},
    'monster' : None,
    'boss' : None,
    'item' : key,
    'trap' : False
}

r5 = {
    'name' : 'room 5',
    'position' : 'position5',
    'description' :"""There's a potion in the room.""",
    'exits' : {'north' : 'rm7', 'west' : 'rm4'},
    'monster' : 2,
    'boss' : None,
    'item' : potion,
    'trap' : False
}

r6 = {
    'name' : 'room 6',
    'position' : 'position6',
    'description' :"""There's a potion in the room.""",
    'exits' : {'north' : 'rm8'},
    'monster' : 2,
    'boss' : None,
    'item' : potion,
    'trap' : False
}

r7 = {
    'name' : 'room 7',
    'position' : 'position7',
    'description' :"""There's a potion in the room.""",
    'exits' : {'north' : 'bossrm', 'east' : 'rm8', 'south' : 'rm5'},
    'monster' : 3,
    'boss' : None,
    'item' : potion,
    'trap' : False
}

r8 = {
    'name' : 'room 8',
    'position' : 'position8',
    'description' :"""There's a potion in the room.""",
    'exits' : {'east' : 'rm9', 'west' : 'rm7'},
    'monster' : 3,
    'boss' : None,
    'item' : potion,
    'trap' : False
}

r9 = {
    'name' : 'room 9',
    'position' : 'position9',
    'description' :"""There's a potion in the room.""",
    'exits' : {'west': 'rm8'},
    'monster' : 3,
    'boss' : None,
    'item' : potion,
    'trap' : False
}

boss = {
    'name' : 'boss room',
    'position' : 'position_boss',
    'description' :"""This is the room where the final boss stands. Legends has it that noone has defeted him before.""",
    'exits' : {},
    'monster' : None,
    'boss' : kirill_riding_a_bear,
    'item' : None,
    'trap' : False
}

start = {
    'name' : 'start',
    'position' : 'position_start',
    'description' :"""You woke up in this dark room. Unknown where you are.""",
    'exits' : {'north' : 'rm2'},
    'monster' : None,
    'boss' : None,
    'item' : None
}

rooms = {
    'rm1' : r1,
    'rm2' : r2,
    'rm3' : r3,
    'rm4' : r4,
    'rm5' : r5,
    'rm6' : r6,
    'rm7' : r7,
    'rm8' : r8,
    'rm9' : r9,
    'bossrm' : boss,
    'startrm' : start
}

dropped_items = []
