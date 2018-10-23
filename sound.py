#Python3 sound.py
import winsound
import os
from time import sleep

def play_sound():
    winsound.PlaySound(os.getcwd() + '\\sample\\rolemu_-_La_Calahorra' , winsound.SND_LOOP|winsound.SND_ASYNC)
    #Music: La Calahorra by Rolemusic http://freemusicarchive.org/
    
def stop_sound():
    winsound.PlaySound(None, winsound.SND_LOOP|winsound.SND_ASYNC)
    
def game_over_sound():
    winsound.PlaySound(None, winsound.SND_LOOP|winsound.SND_ASYNC)
    winsound.Beep(523, 250)
    sleep(0.25)
    winsound.Beep(392, 250)
    sleep(0.25)
    winsound.Beep(329, 250)
    sleep(0.25)
    winsound.Beep(261, 3000)
    

def move_sound():
    winsound.PlaySound(os.getcwd() + '\\sample\\Dress_shoe_jog_on_concrete', winsound.SND_LOOP|winsound.SND_ASYNC)
    #Sound: Dress shoe jog on concrete https://www.youtube.com/audiolibrary/soundeffects/
    sleep(2)
    winsound.PlaySound(os.getcwd() + '\\sample\\rolemu_-_La_Calahorra' , winsound.SND_LOOP|winsound.SND_ASYNC)