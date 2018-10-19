#python3 map.py
r1 = {'name' : 'room 1',
      'position' : 'position1',
      'description' :""" """,
      'exits' : {'north' : 'rm5'}
}

r2 = {'name' : 'room 2',
      'position' : 'position2',
      'description' :""" """,
      'exits' : {'north' : 'rm6', 'east' : 'rm3', 'west' : 'rm1'}
}

r3 = {'name' : 'room 3',
      'position' : 'position3',
      'description' :""" """,
      'exits' : {'west': 'rm2'}
}

r4 = {'name' : 'room 4',
      'position' : 'position4',
      'description' :""" """,
      'exits' : {'east': 'rm5'}
}

r5 = {'name' : 'room 5',
      'position' : 'position5',
      'description' :""" """,
      'exits' : {'north' : 'rm7'}
}

r6 = {'name' : 'room 6',
      'position' : 'position6',
      'description' :""" """,
      'exits' : {'north' : 'rm8'}
}

r7 = {'name' : 'room 7',
      'position' : 'position7',
      'description' :""" """,
      'exits' : {'north' : 'bossrm', 'east' : 'rm8'}
}

r8 = {'name' : 'room 8',
      'position' : 'position8',
      'description' :""" """,
      'exits' : {'east' : 'rm9', 'west' : 'rm7'}
}

r9 = {'name' : 'room 9',
      'position' : 'position9',
      'description' :""" """,
      'exits' : {'west': 'rm8'}
}

boss = {'name' : 'boss room',
        'position' : 'position_boss',
      'description' :""" """,
      'exits' : {}
}

start = {'name' : 'start',
         'position' : 'position_start',
      'description' :""" """,
      'exits' : {'north' : 'rm2'}
}

rooms = {'rm1' : r1,
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
