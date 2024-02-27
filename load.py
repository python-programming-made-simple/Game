import pygame

metal_png = pygame.image.load("metal.png")
start_png = pygame.image.load("start.png")
pause_png = pygame.image.load("pause.png")
lives_png = pygame.image.load("lives.png")
score_png = pygame.image.load("score.png")
background_png = pygame.image.load("background.png")
game_over_png = pygame.image.load("game_over.png")
game_win_png = pygame.image.load("game_win.png")
rocket_png = pygame.image.load("rocket.png")
asteroid_png = pygame.image.load("asteroid.png")

start_sound = pygame.mixer.Sound("start.mp3")
collision_sound = pygame.mixer.Sound("collision.mp3")
pause_sound = pygame.mixer.Sound("pause.mp3")
game_over_sound = pygame.mixer.Sound("game_over.mp3")
game_win_sound = pygame.mixer.Sound("game_win.mp3")
point_sound = pygame.mixer.Sound("point.mp3")

asteroids = []
score = 0
lives = 3