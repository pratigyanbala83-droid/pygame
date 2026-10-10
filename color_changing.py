import pygame, random
pygame.init()
screen = pygame.display.set_mode((500,500))
abc = True
def rand():
    return random.choices(range(256),k=3)
while abc:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,rand(),pygame.Rect(40,40,70,70))
    pygame.display.flip()



