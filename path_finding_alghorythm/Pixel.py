import pygame


#COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Pixel(pygame.sprite.Sprite):
    """description of class"""
        
    def __init__(self, x, y, color = BLACK):
        self.height = 20
        self.width = 20
        self.block = False

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.height, self.width))

        self.color = color
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.center = x+self.width/2, y+self.height/2


    def set_color(self, color: tuple):
        self.image.fill(color)
        self.color = color

    def set_block(self):
        self.set_color(WHITE)
        self.block = True
      
        
    
        
        
        
    def get_coordinates(self):
        return self.rect.center





