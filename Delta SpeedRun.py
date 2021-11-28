import pygame
from pygame.locals import *
import random
from pygame.constants import *
from pygame.locals import *
from pygame import mixer

pygame.init()
pygame.display.init
screen=pygame.display.set_mode([1080,720],HWSURFACE | DOUBLEBUF | RESIZABLE)
#screen = pygame.display.set_mode([1080, 720])
caption = pygame.display.set_caption('Delta SpeedRun')
icon=pygame.image.load('racing.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('wallpaperstart.png')
bg = pygame.transform.scale(bg, (1080, 720))
bg2=pygame.image.load('screen2.png')
bg2 = pygame.transform.scale(bg2, (1080, 720))

#mixer audio
mixer.init()
mixer.music.load("bgmusic.mp3")
mixer.music.play(-1)

start_img = pygame.image.load('buttonstart.png')
start_img1 = pygame.image.load('buttonstart1.png')
exit_img = pygame.image.load('buttonexit.png')
exit_img1 = pygame.image.load('buttonexit2.png')
easy_img=pygame.image.load('buttoneasy.png')
easy_img1=pygame.image.load('buttoneasy1.png')
hard_img=pygame.image.load('buttonhard.png')
hard_img1=pygame.image.load('buttonhard1.png')
torture_img=pygame.image.load('buttontorture.png')
torture_img1=pygame.image.load('buttontorture1.png')

start_img = pygame.transform.scale(start_img, (190, 69))
start_img1 = pygame.transform.scale(start_img1, (190, 69))
exit_img=pygame.transform.scale(exit_img, (190, 69))
exit_img1=pygame.transform.scale(exit_img1, (190, 69))
easy_img=pygame.transform.scale(easy_img, (190, 69))
easy_img1=pygame.transform.scale(easy_img1, (190, 69))
hard_img=pygame.transform.scale(hard_img, (190, 69))
hard_img1=pygame.transform.scale(hard_img1, (190, 69))
torture_img=pygame.transform.scale(torture_img, (190, 69))
torture_img1=pygame.transform.scale(torture_img1, (190, 69))

clock=pygame.time.Clock()

run=True
run2=True
while run:
    clock.tick(30)
    click=False
    screen.blit(bg,(0,0))
    screen.blit(start_img1,(470,300))
    screen.blit(exit_img,(470,400))
    mousepos=pygame.mouse.get_pos()
    exit_rect=exit_img.get_rect(x=470,y=400)
    if exit_rect.collidepoint(mousepos):
            screen.blit(exit_img1,(470,400))
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                run2=False
                run=False
    
    start_rect=start_img.get_rect(x=470,y=300)
    if start_rect.collidepoint(mousepos):
            screen.blit(start_img,(470,300))
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                run2=True
                run=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run2=False
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                run2=False
                run=False

    pygame.display.update()

while run2:
    clock.tick(30)
    screen.blit(bg2,(0,0))
    screen.blit(easy_img1,(120,200))
    screen.blit(hard_img1,(120,300))
    screen.blit(torture_img1,(120,400))
    mousepos=pygame.mouse.get_pos()
    easy_rect=easy_img1.get_rect(x=120,y=200)
    hard_rect=hard_img1.get_rect(x=120,y=300)
    torture_rect=torture_img1.get_rect(x=120,y=400)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            run2=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                run=False
                run2=False

    if easy_rect.collidepoint(mousepos):
            screen.blit(easy_img,(120,200))
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                mixer.music.set_volume(0)
                execfile('Easymode.py')
                break

    elif hard_rect.collidepoint(mousepos):
            screen.blit(hard_img,(120,300))
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                mixer.music.set_volume(0)
                execfile('Hardmode.py')
                break

    elif torture_rect.collidepoint(mousepos):
            screen.blit(torture_img,(120,400))
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                mixer.music.set_volume(0)
                execfile('torture modd.py')
                break

    pygame.display.update()

pygame.quit()    


