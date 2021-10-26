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


while True:
    events = pygame.event.get()
    mouse = pygame.mouse
    for event in events:
        if event.type == pygame.MOUSEMOTION and mouse.get_pressed()[0] == 1:
            pos = mouse.get_pos()
            sprite = window.find_sprite(pos[0], pos[1])
            try:
                sprite.set_block()
            except:
                print("Miss")
    window.screen.fill(WHITE)
    window.all_sprites.draw(window.screen)
    pygame.display.flip()

pygame.quit()