import booleans
import load

def pause(window):
    load.pause_sound.play()
    booleans.started_game = False
    booleans.button_pressed = True
    window.blit(load.start_png,(10,730))