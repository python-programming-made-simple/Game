import booleans as bln
import load

def start(window):
    load.start_sound.play() 
    bln.started_game = True 
    bln.button_pressed = True 
    window.blit(load.pause_png,(10,730)) 