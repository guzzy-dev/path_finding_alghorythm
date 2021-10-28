import pygame
import Pixel

class Window(object):
    """description of class"""
    def __init__(self):
        self.height = 992
        self.width = 992
        self.current_step = []
        self.previous_step = []
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
            coords = sprite.get_coords()
            sprite_x = coords['x']
            sprite_y = coords['y']
            
            if (x >= sprite_x-sprite.width/2 and x <= sprite_x+sprite.width/2):
                if (y >= sprite_y-sprite.height/2 and y <= sprite_y+sprite.height/2):
                    return sprite
    

    def make_bounds(self):
        """
        Function bounds each node with his neighbors by just trying to find neighbor by coordinates 
        via function find_sprite
                    
                          node.up
                            ^
            node.left  <  node  >  node.right
                           \/
                       node.down
        
        """
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
            #print(pixel_x, pixel_y, (pixel.up, pixel.right, pixel.down, pixel.left))



    def start_A_star(self):
        #Find start
        start_pixel = None
        for pixel in self.all_sprites:
            start_pixel = pixel if pixel.start is True else None
            
            if start_pixel is not None: break

        self.current_step.append(start_pixel)
        

    def step_visiting(self): 
        #print(self.current_step)
        next_step = []
        for pixel in self.current_step:
            neighbors = pixel.get_neighbors()
            for neighbor in neighbors:
                if neighbor is not None:                    
                    if neighbor.check_block_and_visited():
                        next_step.append(neighbor)
                        neighbor.visit(pixel)
        #self.previous_step = self.current_step
        self.current_step = next_step

        return self.check_end()
        



    def check_end(self):
        for pixel in self.current_step:
            if pixel.end:
                return(pixel)

    def make_path(self, pixel):
        while pixel is not None:
            #pixel.set_color((255,0,255))
            print(pixel.get_coords())
            pixel.set_path()
            pixel = pixel.previous