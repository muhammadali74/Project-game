import pygame
from pygame.locals import *
import time
import os
import sys
import math
import random
from pygame.constants import *
from pygame.locals import *

pygame.init()
pygame.display.init
screen=pygame.display.set_mode([1080,720],HWSURFACE | DOUBLEBUF | RESIZABLE)
caption=pygame.display.set_caption('Delta SpeedRun')
icon=pygame.image.load('racing.png')
pygame.display.set_icon(icon)

fps=60
clock=pygame.time.Clock()

bg=pygame.image.load('background1.png')
bg=pygame.transform.scale(bg,(1080,720))
bgY=0
bgY2=bg.get_height()

car1=pygame.image.load('car.png')       #<div>Icons made by <a href="https://www.flaticon.com/authors/mynamepong" title="mynamepong">mynamepong</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
car2=pygame.image.load('car2.png')      #<div>Icons made by <a href="https://www.flaticon.com/authors/berkahicon" title="berkahicon">berkahicon</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
car3=pygame.image.load('car3.png')      #<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#<a href="https://www.vecteezy.com/free-vector/car">Car Vectors by Vecteezy</a>
#<a href="https://www.vecteezy.com/free-vector/car">Car Vectors by Vecteezy</a>

#obstacle tree <a href="https://www.vecteezy.com/free-vector/tree">Tree Vectors by Vecteezy</a>

car1=pygame.transform.scale(car1,(120,120))
car2=pygame.transform.scale(car2,(120,120))
car3=pygame.transform.scale(car3,(120,120))
xaxis = 500
yaxis = 570
xc=0
yc=0

def car(pic,xcor,ycor):
    screen.blit(pic,(xcor,ycor))
    
obs1=pygame.image.load('tree1.png')
obs2=pygame.image.load('tree2.png')
obs3=pygame.image.load('tree3.png')
obs4=pygame.image.load('tree4.png')
obs5=pygame.image.load('tree5.png')
obs6=pygame.image.load('cones.png')

obs1=pygame.transform.scale(obs1,(54,54))
obs2=pygame.transform.scale(obs2,(54,54))
obs3=pygame.transform.scale(obs3,(54,54))
obs4=pygame.transform.scale(obs4,(54,54))
obs5=pygame.transform.scale(obs5,(54,54))
obs6=pygame.transform.scale(obs6,(54,54))

xobs = random.randint(180,790)
yobs = -100
xcobs=5
ycobs=5

def obstacle(img,xcor,ycor):
    screen.blit(img,(xcor,ycor))

def redrawWindow():
    screen.blit(bg,(0,bgY))
    screen.blit(bg,(0,bgY2))
    #pygame.display.update()

def collission(x1,y1,x2,y2):
    distance=math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(distance)
    if distance<50:
        return True
    else:
        return False
    
bullet=pygame.image.load('bullet.png')
bullet=pygame.transform.scale(bullet,(28,28))
xbullet=0
ybullet=yaxis
xcbullet=0
ycbullet=-10
bullet_state='hold'

def goli(image,xcor,ycor):
    global bullet_state
    bullet_state='fire'
    screen.blit(image,(xcor+40,ycor+10))

speed=120
pygame.time.set_timer(USEREVENT+1,500)
a=True
while a:
    # x=screen.fill((0,99,0))
    screen.blit(bg,(0,bgY2))
    # xaxis-=0.1
    # yaxis-=0.1
    redrawWindow()
    #clock.tick(speed)
    bgY += 5
    bgY2 +=5
    
    if bgY>=bg.get_height():
        bgY=0
    if bgY2>=bg.get_height()*1:
        bgY2=bg.get_height()*-1
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            a=False
        if event.type==USEREVENT+1:
            speed +=5
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                a=False
            if event.key==pygame.K_LEFT:
                xc=-5
            if event.key==pygame.K_RIGHT:
                xc=5
            if event.key==pygame.K_UP:
                yc=-5
            if event.key==pygame.K_DOWN:
                yc=5
            if event.key==pygame.K_SPACE and bullet_state=='hold':
                xbullet=xaxis
                goli(bullet, xbullet,ybullet)
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                xc=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                yc=0
                
    clock.tick(speed)
                
    xaxis+=xc
    yaxis+=yc
    if xaxis<=180:
        xaxis=180
    if xaxis>=790:
        xaxis=790
    if yaxis<=40:
        yaxis=40
    if yaxis>=600:
        yaxis=600
    
    obstacle(obs6,xobs,yobs)
    yobs+=ycobs
    # if yobs>=625:
    #     yobs=625

    did_collide=collission(xaxis,yaxis,xobs,yobs)
    if did_collide==True:
        print(1)
        xaxis=0
        yaxis=0

    if ybullet<=0:
        bullet_state='hold'
        ybullet=yaxis
    if bullet_state is 'fire':
        goli(bullet,xbullet,ybullet)
        ybullet+=ycbullet

    car(car1,xaxis,yaxis)
        



    pygame.display.update()
    # for i in range(255):
    #     x=screen.fill((0,i,0))
    #     time.sleep(1)
    #     screen.blit(x,(0,0))
    #     pygame.display.update()

    

pygame.quit()
