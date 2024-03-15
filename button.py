import pygame

class Button:
    def __init__(self,x,y,image):
        self.rectangle = image.get_rect()
        self.rectangle.topleft = (x,y)
    def left_click(self):
        cursor_position = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(cursor_position):
            if pygame.mouse.get_pressed()[0] == True:
                return True 
            else: 
                return False 