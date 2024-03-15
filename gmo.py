import load
import booleans as bln

def gmo(window,score_image,lives_image):
    load.game_over_sound.play() 
    window.blit(load.metal_png,(0,720))  
    score_image.display(str(load.score))  
    lives_image.display(str(0))  
    load.asteroids = []  
    bln.button_pressed = True  
    bln.started_game = False  
    bln.game_over = True  