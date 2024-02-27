import load
import booleans

def win(window,score_image,lives_image):
    load.game_win_sound.play()
    window.blit(load.metal_png,(0,720))
    score_image.display(str(load.score))
    lives_image.display(str(load.lives))
    load.asteroids = []
    booleans.button_pressed = True
    booleans.started_game = False
    booleans.game_won = True
    load.score = -1
