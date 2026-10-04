import pygame
pygame.init()

screen = pygame.display.set_mode((300,700))
s = pygame.image.load("space1.jpeg")
s=  pygame.transform.scale(s,(300,700))

while not False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    screen.fill((0,234,12))
    screen.blit(s,(34,78))
    pygame.display.flip()