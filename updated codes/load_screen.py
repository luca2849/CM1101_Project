#python3 load_screen.py
import os
from time import sleep
import random

def print_load_screen(percentage):
    dashes = 100
    
    dash_convert = 100/dashes
    current_dashes = int(percentage/dash_convert)
    remaining_percentage = dashes - current_dashes

    percentage_display = ''.join(['-' for i in range(current_dashes)])
    remaining_display = ''.join([' ' for i in range(remaining_percentage)])
    print("Loading: ""|" + percentage_display + remaining_display + "|", str(percentage) + "%")


def load_screen():
    os.system('cls')
    percentage = 0
    for i in range(10):
        print_load_screen(percentage)
        percentage += int(random.uniform(7,10))
        sleep(0.3)
        os.system('cls')
    percentage = 99
    print_load_screen(percentage)
    sleep(3)
    os.system('cls')
    percentage = 101
    print_load_screen(percentage)
    sleep(1)
    print("Just kidding. (◦ ’ 3 ˉ ◦)")
    sleep(1.5)
    os.system('cls')