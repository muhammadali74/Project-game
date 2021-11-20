import pygame
import time

pygame.init()
pygame.display.init
# flags=OPENGL
# FULLSCREEN
screen=pygame.display.set_mode([1080,720])
caption=pygame.display.set_caption('Delta SpeedRun')

color=0
a=True
while a:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            a=False
    for event in pygame.event.get():
        while color<255:
            screen.fill((255-color,color,0))
            color+=1
            time.sleep(1)
            pygame.display.flip()

    pygame.display.flip()

pygame.quit()