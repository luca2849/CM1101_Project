#Python 3 mapfun.py

def ascii_map():
    position_dict = {'position_boss' : ' ', 'position7' : ' ', 'position8' : ' ', 
                 'position9' : ' ', 'position_mini' : ' ', 'position4' : ' ', 
                 'position5' : ' ', 'position6' : ' ','position1' : ' ', 
                 'position2' : ' ', 'position3' : ' ', 'position_start' : ' '}
    
    '''for key in position_dict:
        if current_room['position'] == key:
            position_dict[key] = '♦'
    '''
            
    lines = [[] for i in range(37)]

    lines[0].append('          ┌────────┐                    ')
    lines[1].append('          |        |                    ')
    lines[2].append('          |        |                    ')
    lines[3].append('          |  FINAL |                    ')
    lines[4].append('          |  BOSS  |                    ')
    lines[5].append('          └───┐┌───┘                    ')
    lines[6].append('          ┌───┘└───┐┌────────┐┌────────┐')
    lines[7].append('          |        ||        ||        |')
    lines[8].append('          |        └┘        └┘        |')
    lines[9].append('          |        ┌┐        ┌┐        |')
    lines[10].append('          |        ||        ||        |')
    lines[11].append('          └───┐┌───┘└───┐┌───┘└────────┘')
    lines[12].append('┌────────┐┌───┘└───┐┌───┘└───┐          ')
    lines[13].append('|        ||        ||        |          ')
    lines[14].append('|        └┘        ||        |          ')
    lines[15].append('|        ┌┐        ||        |          ')
    lines[16].append('|        ||        ||        |          ')
    lines[17].append('└────────┘└───┐┌───┘└───┐┌───┘          ')
    lines[18].append('          ┌───┘└───┐┌───┘└───┐┌────────┐')
    lines[19].append('          |        ||        ||        |')
    lines[20].append('          |        └┘        └┘        |')
    lines[21].append('          |        ┌┐        ┌┐        |')
    lines[22].append('          |        ||        ||        |')
    lines[23].append('          └────────┘└───┐┌───┘└────────┘')
    lines[24].append('                    ┌───┘└───┐          ')
    lines[25].append('                    |        |          ')
    lines[26].append('                    |        |          ')
    lines[27].append('                    |ENTRANCE|          ')
    lines[28].append('                    |        |          ')
    lines[29].append('                    └────────┘          ')
    lines[30].append('♦ IS YOUR POSITION')
    
    result = []
    for item in lines:
        result.append(''.join(item))
        
    return '\n'.join(result)

#current_room = rooms["room_3"]

print(ascii_map())