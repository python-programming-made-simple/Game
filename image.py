import pygame

class Image:
    def __init__(self,window,position,png,png_position):
        self.window = window 
        self.position = position 
        self.png = png 
        self.png_position = png_position 
    def display(self,my_string):
        my_font = pygame.font.SysFont("Arial",16)
        white = (255,255,255)
        number = my_font.render(my_string.zfill(3),True,white)
        self.window.blit(self.png,self.png_position)
        self.window.blit(number,self.position)
        
