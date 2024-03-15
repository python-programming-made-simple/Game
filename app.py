import pygame
pygame.init()
import load
import image 

import rocket as rkt 
import button 
import booleans as bln 
import start 
import pause 
import asteroid as ast 
import collide
import gmo 
import score 
import game_win 

window = pygame.display.set_mode((1280,790))

window.blit(load.background_png,(0,0))
window.blit(load.metal_png,(0,720))
window.blit(load.start_png,(10,730))

p_1 = (1232,752) 
p_2 = (1220,730) 
score_image = image.Image(window,p_1,load.score_png,p_2) 
p_3 = (1172,752) 
p_4 = (1160,730) 
lives_image = image.Image(window,p_3,load.lives_png,p_4) 
score_image.display(str(load.score)) 
lives_image.display(str(load.lives)) 

rocket = rkt.Rocket(window,load.rocket_png,590,561)
rocket.draw() 

pygame.display.update()

clock_one = pygame.time.Clock() 
start_time_one = pygame.time.get_ticks() 
clock_two = pygame.time.Clock() 
start_time_two = pygame.time.get_ticks() 

start_button = button.Button(10,730,load.start_png) 
pause_button = button.Button(10,730,load.pause_png) 

running = True
while running:
    window.blit(load.background_png,(0,0)) 

    if bln.game_over: 
        window.blit(load.game_over_png,(0,0)) 
    if bln.game_won: 
        window.blit(load.game_win_png,(0,0)) 

    if (not bln.started_game) and (not bln.button_pressed):
        if start_button.left_click():
            start.start(window)
    elif (bln.started_game) and (not bln.button_pressed):
        if pause_button.left_click():
            pause.pause(window)
    elif pygame.mouse.get_pressed()[0] == False:
        if (not bln.game_over) and (not bln.game_won):
            bln.button_pressed = False
    else:
        pass    

    current_time = pygame.time.get_ticks() 

    difference_one = current_time - start_time_one
    if difference_one >= 1000 or len(load.asteroids) == 0:
        start_time_one = current_time
        if bln.started_game == True:
            ast.create_asteroid(window)
    if current_time - start_time_two >= 10:
        start_time_two = current_time
        if bln.started_game == True:
            for asteroid in load.asteroids:
                asteroid.translate_down()   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and bln.started_game:
            if event.key == pygame.K_a:
                rocket.translate_left()
            elif event.key == pygame.K_d:
                rocket.translate_right() 

    if (not bln.game_over) and (not bln.game_won): 
        rocket.draw() 

    for asteroid in load.asteroids:
        if asteroid.y < 649:
            asteroid.draw()
            if rocket.collision(asteroid):
                if load.lives >= 2:
                    collide.collide(lives_image,asteroid)
                else:
                    gmo.gmo(window,score_image,lives_image)
        else:
            score.increase_score(asteroid,score_image)

    if load.score >= 10 and load.score != -1: 
        game_win.win(window,score_image,lives_image) 

    pygame.display.update() 