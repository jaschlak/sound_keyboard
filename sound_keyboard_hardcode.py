# -*- coding: utf-8 -*-


import keyboard
import vlc


while True:
    
    if keyboard.is_pressed('1'):
        player = vlc.MediaPlayer("input/1.wav")
        player.play()
        
    if keyboard.is_pressed('2'):
        player = vlc.MediaPlayer("input/2.wav")
        player.play()
        
    if keyboard.is_pressed('3'):
        player = vlc.MediaPlayer("input/3.wav")
        player.play()
        
    if keyboard.is_pressed('4'):
        player = vlc.MediaPlayer("input/4.wav")
        player.play()
        
    if keyboard.is_pressed('5'):
        player = vlc.MediaPlayer("input/5.wav")
        player.play()
        
    if keyboard.is_pressed('6'):
        player = vlc.MediaPlayer("input/6.wav")
        player.play()
        
    if keyboard.is_pressed('7'):
        player = vlc.MediaPlayer("input/7.wav")
        player.play()
        
    if keyboard.is_pressed('z'):
        break
    
    