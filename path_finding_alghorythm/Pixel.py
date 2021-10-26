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
        pygame.sprite.Sprite.__init__(self)
        self.height = 20
        self.width = 20
        self.image = pygame.Surface((self.height, self.width))

        self.color = color
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.center = x+self.width/2, y+self.height/2


    def set_color(color: tuple):
        self.image.fill(color)
        self.color = color



