import pygame
import time
import os
import sys
import random
from pygame.constants import *
from pygame.locals import *

pygame.init()
pygame.display.init
screen=pygame.display.set_mode([1080,720],HWSURFACE | DOUBLEBUF | RESIZABLE)
caption=pygame.display.set_caption('Delta SpeedRun')
icon=pygame.image.load('racing.png')
pygame.display.set_icon(icon)

car1=pygame.image.load('car.png')       #<div>Icons made by <a href="https://www.flaticon.com/authors/mynamepong" title="mynamepong">mynamepong</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
car2=pygame.image.load('car2.png')      #<div>Icons made by <a href="https://www.flaticon.com/authors/berkahicon" title="berkahicon">berkahicon</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
car3=pygame.image.load('car3.png')      #<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#<a href="https://www.vecteezy.com/free-vector/car">Car Vectors by Vecteezy</a>
#<a href="https://www.vecteezy.com/free-vector/car">Car Vectors by Vecteezy</a>

bg=pygame.image.load('Road pic 1 filter.png')
bgY=0
bgY2=bg.get_height()

car1=pygame.transform.scale(car1,(88,88))
car2=pygame.transform.scale(car2,(88,88))
car3=pygame.transform.scale(car3,(88,88))
xaxis = 500
yaxis = 570
xhange=0
yhange=0

def car(pic,xcor,ycor):
    screen.blit(pic,(xcor,ycor))

car1=pygame.transform.scale(car1,(88,88))
car2=pygame.transform.scale(car2,(88,88))
car3=pygame.transform.scale(car3,(88,88))
xobs = 500
yobs = 50
xhangeobs=0
yhangeobs=0

def obstacle(img,xcor,ycor):
    screen.blit(img,((xcor,ycor)))
    
def redrawWindow():
    win.blit(bg, (bgY,0))
    win.blit(bg, (bgY2,0))
    pygame.display.update()

a=True
speed=30
pygame.time.set_timer(Event+1,500)  # speed changes after 500 milisecond
while a:
    x=screen.fill((0,255,0))
    # xaxis-=0.1
    # yaxis-=0.1
    redrawWindow()
    bgY -= 1.4
    bgY2 -= 1.4
    
    if bgY<bg.get_height()*-1:
        bgY=bg.get_height()
    if bgY2<bh.get_height()*-1:
        bgY2=bg.get_height()
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            a=False
        if event.type==Event + 1:
            speed +=1
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                a=False
            if event.key==pygame.K_LEFT:
                xhange=-0.2
            if event.key==pygame.K_RIGHT:
                xhange=0.2
            if event.key==pygame.K_UP:
                yhange=-0.2
            if event.key==pygame.K_DOWN:
                yhange=0.2
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                xhange=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                yhange=0
    clock.tick(speed)
                
    xaxis+=xhange
    yaxis+=yhange
    if xaxis<=0:
        xaxis=0
    if xaxis>=992:
        xaxis=992
    if yaxis<=0:
        yaxis=0
    if yaxis>=625:
        yaxis=625
    car(car1,xaxis,yaxis)

    obstacle(car2,xobs,yobs)
    pygame.display.update()
    # for i in range(255):
    #     x=screen.fill((0,i,0))
    #     time.sleep(1)
    #     screen.blit(x,(0,0))
    #     pygame.display.update()

    

pygame.quit()
