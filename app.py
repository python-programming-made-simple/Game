import pygame
pygame.init()
import load
import image
import rocket as rocket_module
import button
import booleans
import start
import pause
import asteroid as asteroid_module
import collide
import game_over
import score
import game_win

window = pygame.display.set_mode((1280,790))

window.blit(load.background_png,(0,0))
window.blit(load.metal_png,(0,720))
window.blit(load.start_png,(10,730))

score_image = image.Image(window,(1232,752),load.score_png,(1220,730))
lives_image = image.Image(window,(1172,752),load.lives_png,(1160,730))
score_image.display(str(load.score))
lives_image.display(str(load.lives))

rocket = rocket_module.Rocket(window,load.rocket_png,590,561)
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

    if booleans.game_over:
        window.blit(load.game_over_png,(0,0))

    if booleans.game_won:
        window.blit(load.game_win_png,(0,0))

    if (booleans.started_game == False) and (booleans.button_pressed == False):
        if start_button.left_click():
            start.start(window)
    elif booleans.started_game == True and booleans.button_pressed == False:
        if pause_button.left_click():
            pause.pause(window)
    elif pygame.mouse.get_pressed()[0] == False:
        if (not booleans.game_over) and (not booleans.game_won):
            booleans.button_pressed = False
    else:
        pass

    current_time = pygame.time.get_ticks()

    if current_time - start_time_one >= 1000 or len(load.asteroids) == 0:
        start_time_one = current_time
        if booleans.started_game == True:
            asteroid_module.create_asteroid(window)

    if current_time - start_time_two >= 10:
        start_time_two = current_time
        if booleans.started_game == True:
            for asteroid in load.asteroids:
                asteroid.translate_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and booleans.started_game == True:
                rocket.translate_left()
            elif event.key == pygame.K_d and booleans.started_game == True:
                rocket.translate_right()

    if (not booleans.game_over) and (not booleans.game_won):
        rocket.draw()

    for asteroid in load.asteroids:
        if asteroid.y < 649:
            asteroid.draw()
            if rocket.collision(asteroid):
                if load.lives >= 2:
                    collide.collide(lives_image,asteroid)
                else:
                    game_over.game_over(window,score_image,lives_image)
        else:
            score.increase_score(asteroid,score_image)

    if load.score >= 10 and load.score != -1:
        game_win.win(window,score_image,lives_image)


    pygame.display.update()
