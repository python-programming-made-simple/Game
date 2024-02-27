import game_object

class Rocket(game_object.GameObject):
    step = 10
    def translate_left(self):
        if self.x >= self.step:
            self.x = self.x - self.step
    def translate_right(self):
        if self.x + 100 <= 1280 - self.step:
            self.x = self.x + self.step
    def collision(self,asteroid):
        asteroid_rectangle = asteroid.image.get_rect()
        asteroid_rectangle.topleft = (asteroid.x,asteroid.y)
        rocket_rectangle = self.image.get_rect()
        rocket_rectangle.topleft = (self.x,self.y)
        if rocket_rectangle.colliderect(asteroid_rectangle):
            return True
        else:
            return False  