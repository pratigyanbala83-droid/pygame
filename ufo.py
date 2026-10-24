import pygame,math,random

psx = 370
psy =220
sw = 800
sh = 400
collision = 28
esx = 2
esy = 20
got = psy -20
bullet_speed = 10


pygame.init()
screen = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Space invader")

icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
player = pygame.image.load("player.png")
en = pygame.image.load("enemy.png")
bullet = pygame.image.load("bullet.png")
bg = pygame.image.load("background.png")


font = pygame.font.Font("freesansbold.ttf",32)
overfont = pygame.font.Font("freesansbold.ttf",64)

enemy = [{

"x": random.randint(0, sw - 64),

"y": random.randint(50, 150),

"dx": esx

} for _ in range(6)]

bx = 0
by = psy
bs = "ready"

px,py = psx,psy
px_c = 0
score = 0


def showscore():
    score1 = font.render(f"Score: {score}",True,(255,255,255))
    screen.blit(score1,(10,10))
def over():
    over1 = overfont.render(f"Game over",True,(255,255,255))
    screen.blit(over1,(200,250))
def dp():
    screen.blit(player,(px,py))
def ep(enemy):
    screen.blit(en, (enemy["x"], enemy['y']))
def bull():
    screen.blit(bullet,(bx+10,by+16))
def coll_detect(enemy):

     distance = math.hypot((enemy["x"]+32)-bx,(enemy["y"]+32)-by)
     return distance <collision


running = True
clock = pygame.time.Clock()
while running:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                px_c = -5
            if event.key ==pygame.K_RIGHT:
                px_c = 5
            if event.key ==  pygame.K_SPACE and bs == "ready":
                bx = px+16
                by = py
                bs = "fire"
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
                px_c = 0


    px = max(0,min(px+px_c,sw - 64))



    for i in enemy:
        if i ["y"]>= got:
            for e in enemy:
                 e ["y"] = 2000
            over()
            pygame.display.update()
            pygame.time.wait(2000)
            running = False
            break
        i ["x"] += i  ["dx"]
        if i["x"] <=0 or i ["x"]>=sw-64:
            i["dx"]*= -1
            i["y"] += esy

        if  bs == "fire" and   coll_detect(i):
            by = psy
            bs = "ready"
            score += 1
            i["x"] = random.randint(0,sw-64)
            i["y"] = random.randint(50,150)
        ep(i)

    if bs == "fire":
        bull()
        by -= bullet_speed
        if by <= 0:
            bs = "ready"
            by = psy


    showscore()
    dp()
    pygame.display.update()
    clock.tick(60)




pygame.quit()


        



             




