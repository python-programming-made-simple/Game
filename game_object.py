class GameObject:
    def __init__(self,window,image,x,y):
        self.window = window
        self.image = image
        self.x = x
        self.y = y
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))