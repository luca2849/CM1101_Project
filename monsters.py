#python 3 monsters.py
#import random
#from time import sleep
from items import *

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
zombeez = monster('Zombeez', 'Swarm of Zombeez', 1, [bee_stingers])
computer_on_a_scooter = monster('Computer on a Scooter', '', 1, [ddos_attack_script])
tequila_sheila = monster('Tequila Shelia', '', 1, [broken_bottle])
crabs_with_abs = monster('Crabs with Abs', '''These bad boys have been hitting the gym over the summer. They’ve bulked up big time.
They’ve munched their way through protein, smashed their way through sit ups and injected a metric tonne of steroids.''', 1, [workout_routine])
#Tier 2 Monsters
man_made_mermaid = monster('Man-Made Mermaid', '', 2, [trident])
half_a_giraffe = monster('Half a Giraffe', '', 2, [giraffe_drumstick])
big_horn_unicorn = monster ('Big Horn Unicorn', 'This bad boy has an absolute unit of a horn on his head. That’s it. His horn is just an absolute machine.', 2, [unicorn_spear])
deceased_priest = monster('Deceased Priest', 'He’s just a zombie but dressed as a priest. No one really knows how he got the outfit, he was a plumber before he died.', 2, [holy_hand_gernade])
#Tier 3 Monsters
one_tonne_skeleton = monster('One Tonne Skeleton', 'A big skeleton', 3, [bone_saw])
tyrannosaurus_mex = monster('Tyrannosaurus Mex', 'A spicy mexican dinosaur', 3, [maracas])
dragon_in_a_wagon = monster('Dragon in a Wagon', '', 3, [dragons_breath_spell])
geiger_tiger = monster('Geiger Tiger', '', 3, [nuclear_claws])
#Bosses
kirill_riding_a_bear = monster('Kirill Riding a bear', '', 7, [trophy_for_winning_the_game])



#init list of monsters
monster_list = [zombeez, computer_on_a_scooter, tequila_sheila, crabs_with_abs, man_made_mermaid,half_a_giraffe, big_horn_unicorn, deceased_priest, one_tonne_skeleton, tyrannosaurus_mex, dragon_in_a_wagon, geiger_tiger]

boss_list = [kirill_riding_a_bear] # init list of bosses

boss_hp = 300
max_boss_hp = 300

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
