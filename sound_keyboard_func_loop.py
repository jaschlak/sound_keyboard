# -*- coding: utf-8 -*-


import keyboard
import vlc

def sense_key(key):

    if keyboard.is_pressed(key):
        
        # for some reason key value increasing in function
        key -= 1
        
        print(key)
        player = vlc.MediaPlayer("input/{}.wav".format(key))
        player.play()

while True:
    
    for key in range(2,9):
        sense_key(key)
    
    if keyboard.is_pressed('z'):
        break
