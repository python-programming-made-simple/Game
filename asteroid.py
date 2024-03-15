import load 
import random 

import game_object

class Asteroid(game_object.GameObject):
    def translate_down(self):
        self.y = self.y + 1 

def create_asteroid(window): 
    r = random.randint(0,1205) 
    asteroid = Asteroid(window,load.asteroid_png,r,-30) 
    load.asteroids.append(asteroid) 