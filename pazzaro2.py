#tela
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('fundo.png')
BACKGROUND = pygame.transform.scale(BACKGROUND,(SCREEN_WIDTH, SCREEN_HEIGHT))


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.blit(BACKGROUND, (0,0))

    pygame.display.update()
#Ta tudo errado se é muito burro fi
#Burro 3x Mais
#Tu é Burro 4x mais
