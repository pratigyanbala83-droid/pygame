import pygame
pygame.init()
screen = pygame.display.set_mode((650,650))
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.circle(screen,(255,0,0),(100,100),30)
    pygame.draw.circle(screen,(135,8,8),(50,50),30,15)
    pygame.display.flip()

        
