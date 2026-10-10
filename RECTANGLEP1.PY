import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
done = True

while done:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(218,0,0),pygame.Rect(30,30,70,70))
    pygame.display.flip()
            

