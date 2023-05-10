
import pygame

from pygame.locals import *

 

#tela

SCREEN_WIDTH = 980

SCREEN_HEIGHT = 600

 

class Bird(pygame.sprite.Sprite):


    def __init__(self):

        pygame.sprite.Sprite.__init__(self)


        self.images = [pygame.image.load('passaro1.png').convert_alpha(),

                        pygame.image.load('passaro2.png').convert_alpha()]


        self.current_image = 0


        self.image = pygame.image.load('passaro1.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.rect[0] = SCREEN_WIDTH / 2

        self.rect[1] = SCREEN_HEIGHT / 2


    def update(self):

        self.current_image =(self.current_image + 1) % 2 

        self.image = self.images[ self.current_image]



pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

 

BACKGROUND = pygame.image.load('fundo.png')

BACKGROUND = pygame.transform.scale(BACKGROUND,(SCREEN_WIDTH, SCREEN_HEIGHT))

 

bird_group = pygame.sprite.Group()

bird = Bird()

bird_group.add(bird)

 

clock = pygame.time.Clock()

 

while True:

    clock.tick(15)

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()


    screen.blit(BACKGROUND, (0,0))


    bird_group.update()


    bird_group.draw(screen)


    pygame.display.update()

#desenho_personagem


