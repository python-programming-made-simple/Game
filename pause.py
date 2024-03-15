import booleans as bln
import load

def pause(window):
    load.pause_sound.play() 
    bln.started_game = False 
    bln.button_pressed = True 
    window.blit(load.start_png,(10,730)) 