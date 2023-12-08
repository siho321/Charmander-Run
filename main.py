from tkinter.tix import Tree
import pygame
from res.menu import Menu
from res.settings import *
from res.levels import *
from sprites.tile import Tile
from sprites.level import Level

FONT_SIZE = 36

pygame.init()
pygame.display.set_caption('   Charmander Run')
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
menu = Menu(display, 'menu')
level1 = Level(level1, display, menu)
menu.current_level = level1
start_time = pygame.time.get_ticks()
current_time = 0
font = pygame.font.Font(None, FONT_SIZE)



while True:
    #play level
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    display.fill('black')
    while menu.intro:
        menu.game_intro()
        current_time = pygame.time.get_ticks() - start_time

        # Clear the screen
    
        # Render the timer text
        
    
        # Update the screen
        pygame.display.flip()
        

    level1.run()
    clock.tick(FPS)
    pygame.display.update()
