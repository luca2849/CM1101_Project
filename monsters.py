#python 3 monsters.py
#import random
#from time import sleep


class monster:
    '''Class for adding monsters
       monster_id = monster('monster name', 'description', [drops])
       '''
    def __init__(self, name, description, drops):
        self.name = name
        self.description = description
        self.drops = drops

#monsters        
tyrannosaurus_mex = monster('Tyrannosaurus Mex', 'A spicy mexican dinosaur', ['Maracas'])
dragon_in_a_wagon = monster('Dragon in a Wagon', '', ['Dragons Breath Spell'])
one_tonne_skeleton = monster('One Tonne Skeleton', 'A big skeleton', ['Bone Saw'])
zombeez = monster('Zombeez', 'Swarm of Zombeez', ['Bee Stingers'])
crabs_with_abs = monster('Crabs with Abs', '',['Workout Routine'])
big_horn_unicorn = monster ('Big Horn Unicorn', '', ['Unicorn Spear'])
half_a_giraffe = monster('Half a Giraffe', '', ['Giraffe Drumstick'])
geiger_tiger = monster('Geiger Tiger', '', ['Nuclear Claws'])
computer_on_a_scooter = monster('Computer on a Scooter', '', ['DDOS Attack Script'])
deceased_priest = monster('Deceased Priest', '', ['Holy Water'])
tequila_sheila = monster('Tequila Shelia', '', ['Broken Bottle'])
man_made_mermaid = monster('Man-Made Mermaid', '', ['Trident'])
#bosses
kirill_riding_a_bear = monster('Kirill Riding a bear', '', ['Trophy for Winning the Game'])




monster_list = []

monster_list.append(zombeez)
monster_list.append(crabs_with_abs)
monster_list.append(one_tonne_skeleton)
monster_list.append(half_a_giraffe)
monster_list.append(geiger_tiger)
monster_list.append(tequila_sheila)
monster_list.append(computer_on_a_scooter)
monster_list.append(deceased_priest)
monster_list.append(man_made_mermaid)
monster_list.append(big_horn_unicorn)
monster_list.append(tyrannosaurus_mex)
monster_list.append(dragon_in_a_wagon)


boss_list = []

boss_list.append(kirill_riding_a_bear)

'''
# code for generating a random monster name and description
# replace x,y with range of monster in list.
# rearrange list if needed
  
def print_random_monster(x,y):
    rng = int(random.uniform(x,y))
    print(monster_list[rng].name)
    print(monster_list[rng].description)

# looper with a timer to test print_random_monster(x,y)
# smallest value of x is 0 and largest value of y is print (len(monster_list))
    
while True:
    print_random_monster(0,len(monster_list))
    sleep(1)
'''
