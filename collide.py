import load

def collide(lives_image,asteroid):
    load.collision_sound.play() 
    load.asteroids.remove(asteroid) 
    load.lives = load.lives - 1 
    lives_image.display(str(load.lives)) 