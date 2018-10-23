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
zombeez = monster('Zombeez', '''These little fellas ain't here to make honey. They're here to chew gum and eat brains.
And they're all out of gum.''', 1, [bee_stingers])
computer_on_a_scooter = monster('Computer on a Scooter', '''Half computer, half absolute legend, the raddest dude on earth. He shreds the streets on his 2005 razor scooter with sparks.
All the ladies want him, but none can have him. He’s too dedicated to the scooter life. ''', 1, [ddos_attack_script])
tequila_sheila = monster('Tequila Shelia', '''After a rough few months going through a messy divorce Sheila turned to the
tequila. It was the only thing that gave her love anymore. She is high key an alcoholic
and should probably go see someone but instead she’s stuck in a dungeon''', 1, [broken_bottle])
crabs_with_abs = monster('Crabs with Abs', '''These bad boys have been hitting the gym over the summer. They’ve bulked up big time.
They’ve munched their way through protein, smashed their way through sit ups and injected a metric tonne of steroids.''', 1, [workout_routine])
#Tier 2 Monsters
man_made_mermaid = monster('Man-Made Mermaid', '''Created in a lab off-shore far far away.
Following her escape she took refuge within this dungeon and swears to protect it from any intruders at all costs.''', 2, [trident])
half_a_giraffe = monster('Half a Giraffe', '''He’s yellow, brown and not tall at all. He’s a half the size of a normal giraffe but it’s the size of his heart that matters.
He was outcast by his tribe and then found peace with his height when he was taken in by a tribe of similarly sized big horn unicorns.''', 2, [giraffe_drumstick])
big_horn_unicorn = monster ('Big Horn Unicorn', 'This bad boy has an absolute unit of a horn on his head. That’s it. His horn is just an absolute machine.', 2, [unicorn_spear])
deceased_priest = monster('Deceased Priest', 'He’s just a zombie but dressed as a priest. No one really knows how he got the outfit, he was a plumber before he died.', 2, [holy_hand_gernade])
#Tier 3 Monsters
one_tonne_skeleton = monster('One Tonne Skeleton', '''This absolute unit of a skeleton used to belong to World's Strongest Man Eddie Hall.
He's retired now so he doesn't need it, now it's your problem.''', 3, [bone_saw])
tyrannosaurus_mex = monster('Tyrannosaurus Mex', '''A spicy Mexican dinosaur rocking a fiery sombrero, wielding some deadly maracas and busting some sick dance moves.
Good luck with this big bad boy, you're going to need it.''', 3, [maracas])
dragon_in_a_wagon = monster('Dragon in a Wagon', '''Don't underestimate this fiery little boy, he may not look like much with his little red wagon but he can really put up a fight.
None of the dragons back at home could put up a decent fight, so now he seeks some worthy opponents.''', 3, [dragons_breath_spell])
geiger_tiger = monster('Geiger Tiger', '', 3, [nuclear_claws])
#Bosses
kirill_riding_a_bear = monster('Kirill Riding a bear', '', 7, [trophy_for_winning_the_game])



#init list of monsters
monster_list = [zombeez, computer_on_a_scooter, tequila_sheila, crabs_with_abs, man_made_mermaid,half_a_giraffe, big_horn_unicorn, deceased_priest, one_tonne_skeleton, tyrannosaurus_mex, dragon_in_a_wagon, geiger_tiger]

boss_list = [kirill_riding_a_bear] # init list of bosses

boss_hp = 150
max_boss_hp = 150

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
