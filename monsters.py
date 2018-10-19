#python 3 monsters.py
#import random
#from time import sleep

class monster:
    '''Class for adding monsters
       monster_id = monster('monster name', 'description', tier, [drops])
       '''
    def __init__(self, name, description, tier, drops):
        self.name = name
        self.description = description
        self.tier = tier
        self.drops = drops

# =============        
#   monsters
# =============

#Tier 1 Monsters
zombeez = monster('Zombeez', 'Swarm of Zombeez', 1, ['Bee Stingers'])
computer_on_a_scooter = monster('Computer on a Scooter', '', 1, ['DDOS Attack Script'])
tequila_sheila = monster('Tequila Shelia', '', 1, ['Broken Bottle'])
#Tier 2 Monsters
crabs_with_abs = monster('Crabs with Abs', '', 2, ['Workout Routine'])
man_made_mermaid = monster('Man-Made Mermaid', '', 2, ['Trident'])
half_a_giraffe = monster('Half a Giraffe', '', 2, ['Giraffe Drumstick'])
#Tier 3 Monsters
big_horn_unicorn = monster ('Big Horn Unicorn', '', 3, ['Unicorn Spear'])
deceased_priest = monster('Deceased Priest', '', 3, ['Holy Hand Grenade'])
one_tonne_skeleton = monster('One Tonne Skeleton', 'A big skeleton', 3, ['Bone Saw'])
#Tier 4 Monsters
tyrannosaurus_mex = monster('Tyrannosaurus Mex', 'A spicy mexican dinosaur', 4, ['Maracas'])
dragon_in_a_wagon = monster('Dragon in a Wagon', '', 4, ['Dragons Breath Spell'])
geiger_tiger = monster('Geiger Tiger', '', 4, ['Nuclear Claws'])
#Bosses
kirill_riding_a_bear = monster('Kirill Riding a bear', '', 10, ['Trophy for Winning the Game'])



#init list of monsters
monster_list = [zombeez, computer_on_a_scooter, tequila_sheila, crabs_with_abs, man_made_mermaid,half_a_giraffe, big_horn_unicorn, deceased_priest, one_tonne_skeleton, tyrannosaurus_mex, dragon_in_a_wagon, geiger_tiger]

boss_list = [kirill_riding_a_bear] # init list of bosses


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
