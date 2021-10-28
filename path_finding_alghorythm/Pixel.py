import pygame


#COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 105)

class Pixel(pygame.sprite.Sprite):
    """description of class"""
        
    def __init__(self, x, y, color = BLACK):
        self.height = 20
        self.width = 20
        self.block = False
        self.visited = False
        self.previous = None

        self.start = False
        self.end = False

        self.up = None
        self.down = None
        self.right = None
        self.left = None

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

    def set_start(self):
        self.start = True
        self.visited = True
        self.set_color(RED)
      
    def set_end(self):
        self.end = True
        self.set_color(GREEN)

    def set_path(self):
        self.set_color(BLUE)

    def delete_block(self):
        self.set_color(BLACK)
        self.block = False
    
        
    def visit(self, previous_pixel):
        if self.block is False and self.visited is False:
            self.visited = True
            self.previous = previous_pixel
            self.set_color(YELLOW)


    def check_block_and_visited(self): 
        if self.block is False and self.visited is False:
            return True
        else: return False
        

    def get_neighbors(self):
        return [self.up,
                self.right,
                self.down,
                self.left]


    def get_coords(self):
        return {'x':self.rect.center[0],
                'y':self.rect.center[1]}






