import pygame
import Pixel

class Window(object):
    """description of class"""
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


    def find_sprite(self, x, y):
        for sprite in self.all_sprites:
            coords = sprite.get_coordinates()
            sprite_x = coords[0]
            sprite_y = coords[1]
            
            if (x >= sprite_x-sprite.width/2 and x <= sprite_x+sprite.width/2):
                if (y >= sprite_y-sprite.height/2 and y <= sprite_y+sprite.height/2):
                    return sprite

