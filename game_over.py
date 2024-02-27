import load
import booleans

def game_over(window,score_image,lives_image):
    load.game_over_sound.play()
    window.blit(load.metal_png,(0,720))
    score_image.display(str(load.score))
    lives_image.display(str(0))
    load.asteroids = []
    booleans.button_pressed = True
    booleans.started_game = False
    booleans.game_over = True
