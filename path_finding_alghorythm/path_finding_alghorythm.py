import pygame
import Window

#COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

      
window = Window.Window()
window.create_sprites()
window.make_bounds()


while True:
    events = pygame.event.get()
    mouse = pygame.mouse
    pos = mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEMOTION and mouse.get_pressed()[0] == 1:
            
            sprite = window.find_sprite(pos[0], pos[1])
            try:
                sprite.set_block()
            except:
                pass
        if event.type == pygame.MOUSEMOTION and mouse.get_pressed()[2] == 1:
            sprite = window.find_sprite(pos[0], pos[1])
            try:
                sprite.delete_block()
            except:
                pass


    window.screen.fill(WHITE)
    window.all_sprites.draw(window.screen)
    pygame.display.flip()

