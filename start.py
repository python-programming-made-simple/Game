import booleans
import load

def start(window):
    load.start_sound.play()
    booleans.started_game = True
    booleans.button_pressed = True
    window.blit(load.pause_png,(10,730))