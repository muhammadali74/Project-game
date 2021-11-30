import pygame
from pygame.locals import *
import random
from pygame.constants import *
from pygame.locals import *
from pygame import mixer
 
#initializing pygame, defining canvas size, setting icon and caption of the game.
pygame.init()
pygame.display.init
screen=pygame.display.set_mode([1080,720],HWSURFACE | DOUBLEBUF | RESIZABLE)
#screen = pygame.display.set_mode([1080, 720])
caption = pygame.display.set_caption('Delta SpeedRun')
icon=pygame.image.load('./Misc/racing.png')
pygame.display.set_icon(icon)
#loading background image
bg = pygame.image.load('./backgrounds/wallpaperstart.png')
bg = pygame.transform.scale(bg, (1080, 720))
bg2=pygame.image.load('./backgrounds/screen2.png')
bg2 = pygame.transform.scale(bg2, (1080, 720))

#for playing background music
mixer.init()
mixer.music.load("./Music/bgmusic.mp3")
mixer.music.play(-1)

#loading button images
start_img = pygame.image.load('./buttons/buttonstart.png')
start_img1 = pygame.image.load('./buttons/buttonstart1.png')
exit_img = pygame.image.load('./buttons/buttonexit.png')
exit_img1 = pygame.image.load('./buttons/buttonexit2.png')
easy_img=pygame.image.load('./buttons/buttoneasy.png')
easy_img1=pygame.image.load('./buttons/buttoneasy1.png')
hard_img=pygame.image.load('./buttons/buttonhard.png')
hard_img1=pygame.image.load('./buttons/buttonhard1.png')
torture_img=pygame.image.load('./buttons/buttontorture.png')
torture_img1=pygame.image.load('./buttons/buttontorture1.png')

#resizing button images
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
#initializing clock for frame rate
clock=pygame.time.Clock()

def execfiles(filepath, globals=None, locals=None):  # This function is written using the snippet from https://newbedev.com/what-is-an-alternative-to-execfile-in-python-3
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)

run=True
run2=True
while run:
    clock.tick(30)
    click=False

    #displaying background image and buttons
    screen.blit(bg,(0,0))
    screen.blit(start_img1,(470,300))
    screen.blit(exit_img,(470,400))

    #get mouse position
    mousepos=pygame.mouse.get_pos()

    exit_rect=exit_img.get_rect(x=470,y=400)
    #check if mouse hovers over the exit button
    if exit_rect.collidepoint(mousepos):
            screen.blit(exit_img1,(470,400))
            #exit the game if exit is clicked
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                run2=False
                run=False
    #check if mouse hovers over the start button
    start_rect=start_img.get_rect(x=470,y=300)
    if start_rect.collidepoint(mousepos):
            screen.blit(start_img,(470,300))
            #terminate this loop the game if start is clicked
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                run2=True
                run=False
    for event in pygame.event.get():
        #exit the game if exit is clicked
        if event.type==pygame.QUIT:
            run2=False
            run=False
        #exit the game if Escape key is pressed
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                run2=False
                run=False

    pygame.display.update()

while run2:
    clock.tick(30)
    #displaying background image and buttons
    screen.blit(bg2,(0,0))
    screen.blit(easy_img1,(120,200))
    screen.blit(hard_img1,(120,300))
    screen.blit(torture_img1,(120,400))

    #get mouse position
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
    #check if mouse hovers over the 3 buttons and open the game mode file which corresponds to the button
    if easy_rect.collidepoint(mousepos):
            screen.blit(easy_img,(120,200))
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                mixer.music.set_volume(0)
                execfiles('Easymode.py')
                break

    elif hard_rect.collidepoint(mousepos):
            screen.blit(hard_img,(120,300))
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                mixer.music.set_volume(0)
                execfiles('Hardmode.py')
                break

    elif torture_rect.collidepoint(mousepos):
            screen.blit(torture_img,(120,400))
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                mixer.music.set_volume(0)
                execfiles('torture modd.py')
                break

    pygame.display.update()

pygame.quit()    


