#python 3 monsters.py
#import random
#from time import sleep
from items import *

class monster:
    '''Class for adding monsters
       monster_id = monster('monster name', 'description', tier, [drops], ascii_art)
       '''
    def __init__(self, name, description, tier, drops, ascii_art):
        self.name = name
        self.description = description
        self.tier = tier
        self.drops = drops
        self.ascii_art = ascii_art

# =============        
#   monsters
# =============

#Tier 1 Monsters
zombeez = monster('Zombeez', '''These little fellas ain't here to make honey. They're here to chew gum and eat brains.
And they're all out of gum.''', 1, [bee_stingers], '''
 ,,     ,,     ,,
  oo    _oo_   ,oo,
 /==\   /==\   /==\\
(/==\) (/==\) (/==\)
  \/     \/     \/ ''')
computer_on_a_scooter = monster('Computer on a Scooter', '''Half computer, half absolute legend, the raddest dude on earth. He shreds the streets on his 2005 razor scooter with sparks.
All the ladies want him, but none can have him. He’s too dedicated to the scooter life. ''', 1, [ddos_attack_script], '''
  _________
    / ======= \\
   / __________\\
  | ___________ |
  | | -       | |
  | |         | |
  | |_________| |________________________
  \=____________/                         )
  / """"""""""" \                       /
 / ::::::::::::: \                  =D-'
(_________________)''')
tequila_sheila = monster('Tequila Shelia', '''After a rough few months going through a messy divorce Sheila turned to the
tequila. It was the only thing that gave her love anymore. She is high key an alcoholic
and should probably go see someone but instead she’s stuck in a dungeon.''', 1, [broken_bottle], '''
 /////////////\\\\\\\\
(((((((((((((( \\\\\\\\
))) ~~      ~~  (((
((( (*)     (*) )))
)))     <       (((
((( '\______/`  )))
)))\___________/(((
       _) (_
      / \_/ \\
     /(     )\\
    // )___( \\\\
    \\\\(     )//
     (       )
      |  |  |
       | | |
       | | |
      _|_|_|_ ''')
crabs_with_abs = monster('Crabs with Abs', '''These bad boys have been hitting the gym over the summer. They’ve bulked up big time.
They’ve munched their way through protein, smashed their way through sit ups and injected a metric tonne of steroids.''', 1, [workout_routine], '''
     /\\
    ( /   @ @    ()
     \\\\ __| |__  /
      \/   "   \/
     /-|   ()  |-\\
    / /-\  () /-\ \\
     / /-`---'-\ \\
      /         \  ''')

#Tier 2 Monsters
man_made_mermaid = monster('Man-Made Mermaid', '''Created in a lab off-shore far far away.
Following her escape she took refuge within this dungeon and swears to protect it from any intruders at all costs.''', 2, [trident], '''
             __
               _o8o_o888888oo     _
                 o88888888 ,|    /#\\\\\\
        \`.    /| `o88'88o _/    \_/
         \ `-.' |      __) \__   _Y_
          `-. .-'     /       \ /[_/
            | \      / (_(_ /\ y /
            |  \     \ /.  (  \_/
            |   \     V\____\\\\\\
            \    `-._/      |
             \     _/      /
              \           /
               `-..___..-'
''')
half_a_giraffe = monster('Half a Giraffe', '''He’s yellow, brown and not tall at all. He’s a half the size of a normal giraffe but it’s the size of his heart that matters.
He was outcast by his tribe and then found peace with his height when he was taken in by a tribe of similarly sized big horn unicorns.''', 2, [giraffe_drumstick], '''

      O O
      |_|
    <(+ +)>
     ( u )             o
        \\\\            /
         ------------/
        /|          /|
       //||      ( /||
      // ||______//_||
     //  ||     //  ||
    //   ||    //   ||
    \\\\   ||    \\\\   ||
     \\\\  ||     \\\\  ||
     //  ||     //  ||
    /_\ /__\   /_\ /__\ ''')

big_horn_unicorn = monster ('Big Horn Unicorn', 'This bad boy has an absolute unit of a horn on his head. That’s it. His horn is just an absolute machine.', 2, [unicorn_spear], '''
             ,,))))))));,
           __)))))))))))))),
\|/       -\(((((''((((((((.
-*-==//////((''  .     `)))))),
/|\      ))| o    ;-.    '(((((                                  ,(,
         ( `|    /  )    ;))))'                               ,_))^;(~
            |   |   |   ,))((((_     _____------~~~-.        %,;(;(>';'~
            o_);   ;    )))(((` ~---~  `::           \      %%%%~~)(v;(`('~
                  ;    ''````         `:       `:::|\,__,%%%%    );`'; ~
                 |   _                )     /      `:|`----'     `-'
           ______/\/~    |                 /        /
         /~;;.____/;;'  /          ___--,-(   `;;;/
        / //  _;______;'------~~~~~    /;;/\    /
       //  | |                        / ;   \;;,\\
      (<_  | ;                      /',/-----'  _>
       \_| ||_                     //~;~~~~~~~~~
           `\_|                   (,~~  
                                   \~\\
                                    ~~ ''')
deceased_priest = monster('Deceased Priest', 'He’s just a zombie but dressed as a priest. No one really knows how he got the outfit, he was a plumber before he died.', 2, [holy_hand_gernade], '''
                    #,-. ,-.#
                  () a   e ()
                  (   (_)   )
                  #\_  -  _/#
                ,'   `"""`    `.
              ,'      \X/      `.
             /         X     ____\\
            /          v   ,`  v  `,
           /    /         ( <==+==> )
           `-._/|__________\   ^   /
          (\\\\)  |______@____\  ^  /
            \\\\  |     ( )    \ ^ /
             )  |             \^/
            (   |             |v
           <(^)>|             |
             v  |             |
                |             |
                |_.--.__ .--._|
                  `==='  `===' ''')
#Tier 3 Monsters
one_tonne_skeleton = monster('One Tonne Skeleton', '''This absolute unit of a skeleton used to belong to World's Strongest Man Eddie Hall.

He's retired now so he doesn't need it, now it's your problem.''', 3, [bone_saw], '''
                            _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      )\\
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \\'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \\
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \\
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
                             )(  l\ o ('..-.
                       _..--' _'-' '--'.-. |
                __,,-'' _,,-''            \ \\
               f'. _,,-'                   \ \\
              ()--  |                       \ \\
                \.  |                       /  \\
                  \ \                      |._  |
                   \ \                     |  ()|
                    \ \                     \  /
                     ) `-.                   | |
                    // .__)                  | |
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  \\
                                             |lllj
                                             |||||


''')


tyrannosaurus_mex = monster('Tyrannosaurus Mex', '''A spicy Mexican dinosaur rocking a fiery sombrero, wielding some deadly maracas and busting some sick dance moves.
Good luck with this big bad boy, you're going to need it.''', 3, [maracas], '''____
       ___                                      .-~. /_"-._
      `-._~-.                                  / /_ "~o\  :Y
          \  \                                / : \~x.  ` ')
           ]  Y                              /  |  Y< ~-.__j
          /   !                        _.--~T : l  l<  /.-~
         /   /                 ____.--~ .   ` l /~\ \<|Y
        /   /             .-~~"        /| .    ',-~\ \L|
       /   /             /     .^   \ Y~Y \.^>/l_   "--'
      /   Y           .-"(  .  l__  j_j l_/ /~_.-~    .
     Y    l          /    \  )    ~~~." / `/"~ / \.__/l_
     |     \     _.-"      ~-{__     l  :  l._Z~-.___.--~
     |      ~---~           /   ~~"---\_  ' __[>
     l  .                _.^   ___     _>-y~
      \  \     .      .-~   .-~   ~>--"  /
       \  ~---"            /     ./  _.-'
        "-.,_____.,_  _.--~\     _.-~
                    ~~     (   _}      
                           `. ~(
                             )  \\
                            /,`--'~--\ ''')
dragon_in_a_wagon = monster('Dragon in a Wagon', '''Don't underestimate this fiery little boy, he may not look like much with his little red wagon but he can really put up a fight.
None of the dragons back at home could put up a decent fight, so now he seeks some worthy opponents.''', 3, [dragons_breath_spell], '''
      ( _)                ( _)
            / / \\\\              / /\_\_
           / /   \\\\            / / | \ \\
          / /     \\\\          / /  |\ \ \\
         /  /   ,  \ ,       / /   /|  \ \\
        /  /    |\_ /|      / /   / \   \_\\
       /  /  |\/ _ '_|\    / /   /   \    \\\\
      |  /   |/  0 \\0\ \  / |    |    \    \\\\
      |    |\|      \_\_ /  /    |     \    \\\\
      |  | |/    \.\ o\o)  /      \     |    \\\\
      \    |     /\\\\`v-v  /        |    |     \\\\
       | \/    /_| \\\\_|  /         |    | \    \\\\
       | |    /__/_     /   _____  |    |  \    \\\\
       \|    [__]  \_/  |_________  \   |   \    ()
        /    [___] (    \         \  |\ |   |   //
       |    [___]                  |\| \|   /  |/
      /|    [____]                  \  |/\ / / ||
     (  \   [____ /     ) _\      \  \    \| | ||
      \  \  [_____|    / /     __/    \   / / //
      |   \ [_____/   / /        \    |   \/ //
      |   /  '----|   /=\____   _/    |   / //
   __ /  /        |  /   ___/  _/\    \  | ||
  (/-(/-\)       /   \  (/\/\)/  |    /  | /
                (/\/\)           /   /   //
                       _________/   /    /
                      \____________/    ( ''')
geiger_tiger = monster('Geiger Tiger', '''Chris used to work in a nuclear power plant before the day of the disaster. He just about survived the blast before the severe radiation
transformed him into the Geiger Tiger.''', 3, [nuclear_claws], '''
          __  -==-=_,-.
        /--`' \_@-@.--<
        `--'\ \   <___/.  
             \ \\\\   " /  
              >=\\\\_/`<
  ____       /= |  \_|/
_'    `\   _/=== \___/
`___/ //\./=/~\====\\
    \   // /   | ===:
     |  ._/_,__|_ ==:        __
      \/    \\\\ \\\\`--|       / \\\\
       |    _     \\\\:      /==:-\\
       `.__' `-____/       |--|==:
          \    \ ===\      :==:`-'
          _>    \ ===\    /==/
         /==\   |  ===\__/--/
        <=== \  /  ====\ \\\\/
        _`--  \/  === \/--'
       |       \ ==== |
        -`------/`--' /
                \___-
''')
#Bosses
kirill_riding_a_bear = monster('Kirill Riding a bear', '''Overlord of the Dungeon, overseer of our first module, also a certified absolute legend.
He's all that stands in your way now. Finish him.''', 7, [trophy_for_winning_the_game], '''



                 .-:+syyyso/-
              ./sddmmmmmmmmmhys+:
            yydddmmmmmmmmmmmmmmmy:
          :hdddmmmmmmmmmmmmmmNNmmd+.
         +mmmmdhyso+++++oshdmNmmmdm+`
         ddo+//::-....----/+ymNmmmmd.
         +d/:--........--.--:+hNNmmmd
         yh:----..........--:/ymNmmmd
         hd::::------::/:::-::/dNmNNm+
         ohs+ossosooooosyssyssyydmmyss
         IIIIIII+o-so/IIIIII::/hhy:/o.
         IXXXXX:I-IIIIXXXXXXI=========
         IIIIIII.-:://IIIIII-:::--/s.
           -::/:://///:::///::::::+yy-
           `:::/s/::::/+o:::::::/:+y
            .:-.://////:-.-::////:+s
             `-----::---.-://+/:::oNmo.
               `--.--.--:/++/::::/hNmmd+.```
            .://+os////++++/::--/shmmmmmmmdy+:.```..
        /shdmmmmNm//////::--:oyhhmmmmmmmmmmdddho:..
     .ydmmmmmmmdd+:----::oyhhddmmmmmmmmmmmmmddddmd
    `hdmmmmmmmhdmh::::oyddddddmmmmmmmmmmmmmmmmmmmN
    /dmmmmmmmdhdmm+::odmddddddmmmmmmmmmmmmmmmNNNNN
    ymmmmmmmmmNmmdy-:hmmdyddddmmmmmmmmNmNNmmNNNNNN
    dmmmmmmmmNNdmddosdmmhddhddmmmmmmmmNNNmNNNNNNNN

            ''')



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

print(man_made_mermaid.ascii_art)