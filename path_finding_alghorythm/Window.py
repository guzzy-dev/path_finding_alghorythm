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
        self.space_between_sprites = 2
        x = y = self.space_between_sprites
              
        sprite_side_size = 20
        for x in range(self.space_between_sprites,       self.height,     self.space_between_sprites + sprite_side_size):
           for y in range(self.space_between_sprites,    self.width,      self.space_between_sprites + sprite_side_size):
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
    

    def make_bounds(self):
        for pixel in self.all_sprites:
            pixel_x = pixel.get_coords()['x']
            pixel_y = pixel.get_coords()['y']
            
            try:
                right_pixel = self.find_sprite(pixel_x + pixel.width, pixel_y)
                pixel.right = right_pixel
            except: pass 
            
            try:
                left_pixel = self.find_sprite(pixel_x - pixel.width, pixel_y)
                pixel.left = left_pixel
            except: pass

            try:
                up_pixel = self.find_sprite(pixel_x, pixel_y - pixel.height)
                pixel.up = up_pixel
            except: pass

            try:
                down_pixel = self.find_sprite(pixel_x, pixel_y + pixel.height)
                pixel.down = down_pixel
            except: pass


