import pygame

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

dis=pygame.display.set_mode((2000,1500))

pygame.display.set_caption('Snake Game')

x1=300
y1=300

x1_change=0
y1_change=0

clock=pygame.time.Clock()

green=(0,128,0)
red=(255,0,0)

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

    x1+=x1_change
    y1+=y1_change
    dis.fill(white)
    pygame.draw.rect(dis,green,[400,300,50,50])
    pygame.display.update()
    clock.tick(30)
pygame.quit()

quit()