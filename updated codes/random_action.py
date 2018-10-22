#python3 random.py
from monsters import *
import random

def random_monster(x,y):
    rng = int(random.uniform(x,y))
    return rng

def random_stats(monster_gen):
    tier = monster_list[monster_gen].tier
    HP = int(random.uniform(5 + 5 * tier, 10 + 5 * tier))
    return HP

def random_atk(player_level, equip):
    power = 0
    if equip is None:
        power = 0
    else:
        power = equip['power']
    atk = int(random.uniform(2 + (player_level + power) * 3, 5 + (player_level + power) * 3))
    return atk

def random_monster_atk(monster_gen):
    tier = monster_list[monster_gen].tier
    atk = int(random.uniform(2 + 3 * tier, 5 + 3 * tier))
    return atk

def random_boss_atk(boss):
    tier = boss.tier
    atk = int(random.uniform(2 + 3 * tier, 5 + 3 * tier))
    return atk

def random_boss_atk2(boss):
    tier = boss.tier
    atk = int(random.uniform(3 + 4 * tier, 6 + 4 * tier))
    return atk

def random_drop(monster_gen):
    y = len(monster_list[monster_gen].drops)
    rng = int(random.uniform(0,y))
    return rng
