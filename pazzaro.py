
# o codigo ta deveras poggers

import pygame
from pygame.locals import *

# tela do jogo
titulo = 'pazaro'
screen_width = 640
screen_height = 480

pygame.init()
screen = pygame.display.set_mod((screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update()
