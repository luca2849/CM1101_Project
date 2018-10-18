#Python 3 mapfun.py
from map import *

def ascii_map(current_room):
    position_dict = {'position_boss' : ' ', 'position9' : ' ', 'position8' : ' ', 
                 'position7' : ' ', 'position6' : ' ', 
                 'position5' : ' ', 'position4' : ' ','position3' : ' ', 
                 'position2' : ' ', 'position1' : ' ', 'position_start' : ' '}
    
    for key in position_dict:
        if current_room['position'] == key:
            position_dict[key] = '♦'
    
            
    lines = [[] for i in range(31)]

    lines[0].append('          ┌────────┐                    ')
    lines[1].append('          |        |                    ')
    lines[2].append('          |   {}    |                    '.format(position_dict['position_boss']))
    lines[3].append('          |  FINAL |                    ')
    lines[4].append('          |  BOSS  |                    ')
    lines[5].append('          └───┐┌───┘                    ')
    lines[6].append('          ┌───┘└───┐┌────────┐┌────────┐')
    lines[7].append('          |        ||        ||        |')
    lines[8].append('          |   {}    └┘   {}    └┘   {}    |'.format(position_dict['position7'], position_dict['position8'], position_dict['position9']))
    lines[9].append('          |        ┌┐        ┌┐        |')
    lines[10].append('          |        ||        ||        |')
    lines[11].append('          └───┐┌───┘└───┐┌───┘└────────┘')
    lines[12].append('┌────────┐┌───┘└───┐┌───┘└───┐          ')
    lines[13].append('|        ||        ||        |          ')
    lines[14].append('|   {}    └┘   {}    ||   {}    |          '.format(position_dict['position4'], position_dict['position5'], position_dict['position6']))
    lines[15].append('|        ┌┐        ||        |          ')
    lines[16].append('|        ||        ||        |          ')
    lines[17].append('└────────┘└───┐┌───┘└───┐┌───┘          ')
    lines[18].append('          ┌───┘└───┐┌───┘└───┐┌────────┐')
    lines[19].append('          |        ||        ||        |')
    lines[20].append('          |   {}    └┘   {}    └┘   {}    |'.format(position_dict['position1'], position_dict['position2'], position_dict['position3']))
    lines[21].append('          |        ┌┐        ┌┐        |')
    lines[22].append('          |        ||        ||        |')
    lines[23].append('          └────────┘└───┐┌───┘└────────┘')
    lines[24].append('                    ┌───┘└───┐          ')
    lines[25].append('                    |        |          ')
    lines[26].append('                    |   {}    |          '.format(position_dict['position_start']))
    lines[27].append('                    |ENTRANCE|          ')
    lines[28].append('                    |        |          ')
    lines[29].append('                    └────────┘          ')
    lines[30].append('♦ IS YOUR POSITION')
    
    result = []
    for item in lines:
        result.append(''.join(item))
        
    return '\n'.join(result)

#current_room = rooms["room_3"]

#print(ascii_map())