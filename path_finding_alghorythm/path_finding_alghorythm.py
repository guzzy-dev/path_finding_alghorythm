import pygame
import Pixel

#COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Window():
    def __init__(self):
        self.height = 992
        self.width = 992
        pygame.init()
        self.screen = pygame.display.set_mode((self.height, self.width))
        pygame.display.set_caption('Path finding algorythm')
        self.all_sprites = pygame.sprite.Group()

    
    def add_sprite(self, sprite):
            self.all_sprites.add(sprite)
            self.all_sprites.update()


    def create_sprites(self):
        space_between_sprites = 2
        x = y = space_between_sprites
              
        sprite_side_size = 20
        for x in range(space_between_sprites,       self.height,     space_between_sprites+sprite_side_size):
           for y in range(space_between_sprites,    self.width,      space_between_sprites+sprite_side_size):
                pixel = Pixel.Pixel(x, y)
                self.add_sprite(pixel)





all_sprites = pygame.sprite.Group()


      
window = Window()
window.create_sprites()
while True:
    window.screen.fill(WHITE)
    window.all_sprites.draw(window.screen)
    pygame.display.flip()

pygame.quit()