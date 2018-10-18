#Python3 sound.py
import winsound
import os
from time import sleep

def play_sound():
    winsound.PlaySound(os.getcwd() + '\\sample\\rolemu_-_La_Calahorra' , winsound.SND_LOOP|winsound.SND_ASYNC)

def stop_sound():
    winsound.PlaySound(None, winsound.SND_LOOP|winsound.SND_ASYNC)

def move_sound():
    winsound.PlaySound(os.getcwd() + '\\sample\\Dress_shoe_jog_on_concrete', winsound.SND_LOOP|winsound.SND_ASYNC)
    sleep(2)
    winsound.PlaySound(os.getcwd() + '\\sample\\rolemu_-_La_Calahorra' , winsound.SND_LOOP|winsound.SND_ASYNC)