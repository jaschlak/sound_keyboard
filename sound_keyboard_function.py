# -*- coding: utf-8 -*-


import keyboard
import vlc

def sense_key(key):
    
    if keyboard.is_pressed(key):
        player = vlc.MediaPlayer("input/{}.wav".format(key))
        player.play()

while True:
    
    sense_key('1')
    sense_key('2')
    sense_key('3')
    sense_key('4')
    sense_key('5')
    sense_key('6')
    sense_key('7')
    
    if keyboard.is_pressed('z'):
        break
