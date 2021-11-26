import pygame
from pygame.locals import *
import time
import os
import sys
import math
import random
from pygame.constants import *
from pygame.locals import *
from pygame import mixer

pygame.init()
pygame.display.init
screen=pygame.display.set_mode([1080,720],HWSURFACE | DOUBLEBUF | RESIZABLE)
caption=pygame.display.set_caption('Delta SpeedRun')
icon=pygame.image.load('racing.png')
pygame.display.set_icon(icon)

mixer.init()
mixer.music.load("background.wav")
#mixer.music.set_volume(1)
mixer.music.play(-1)  #-------> to play on loop

fps=60
clock=pygame.time.Clock()

bg=pygame.image.load('background1.png')
bg2=pygame.image.load('Road pic 1 filter.jpg')
bg=pygame.transform.scale(bg,(1080,720))
bg2=pygame.transform.scale(bg2,(1080,720))
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
temp=pygame.transform.scale(car2,(20,100))
xaxis = 500
yaxis = 570
xc=0
yc=0

def car(pic,pictemp,xcor,ycor):
    global carrect
    temp=pygame.transform.scale(pictemp,(40,70))
    carrect=temp.get_rect(x=xcor+50,y=ycor)
    screen.blit(pic,(xcor,ycor))
    
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (245, 255, 250))
    screen.blit(over_text, (200, 250))

obs1=pygame.image.load('tree1.png')
obs2=pygame.image.load('tree2.png')
obs3=pygame.image.load('tree3.png')
obs4=pygame.image.load('tree4.png')
obs5=pygame.image.load('tree5.png')
obs6=pygame.image.load('cones.png')
obs7=pygame.image.load('traffic-barriers.png')
obs8=pygame.image.load('barrier.png')
obs9=pygame.image.load('ditch.png')
obs10=pygame.image.load('obstacle-hole.png')
# all_obstacles=[]
# for i in range(1,11):
#     obsv=pygame.transform.scale((obs+str(i)),(54,54))
    # all_obstacles.append(obsv)



obs1=pygame.transform.scale(obs1,(54,54))
obs2=pygame.transform.scale(obs2,(54,54))
obs3=pygame.transform.scale(obs3,(54,54))
obs4=pygame.transform.scale(obs4,(54,54))
obs5=pygame.transform.scale(obs5,(54,54))
obs6=pygame.transform.scale(obs6,(54,54))
obs7=pygame.transform.scale(obs7,(54,54))
obs8=pygame.transform.scale(obs8,(54,54))
obs9=pygame.transform.scale(obs9,(54,54))
obs10=pygame.transform.scale(obs10,(54,54))

all_obstacles=[obs1,obs2,obs3,obs4,obs5,obs6,obs7,obs8,obs9,obs10]
random_obstacles=random.choice(all_obstacles)
obstacle_num=random.randint(8,10)
obs=[]
xobs=[]
yobs=[]
positionx=[]
positiony=[]
# xobs = random.randint(180,790)
# yobs = -100
ycobs=3
for i in range(obstacle_num):
    random_obstacles=random.choice(all_obstacles)
    obs.append(random_obstacles)
    xobs.append(random.randint(180,790))
    yobs.append(random.randint(-1200,-200))
    positionx.append(random.randint(180,790))
    positiony.append(random.randint(-1200,-200))

def obstacle(img,xcor,ycor):
    global obsrect
    obsrect=img.get_rect(x=xcor,y=ycor)
    screen.blit(img,(xcor,ycor)

def redrawWindow(background):
    screen.blit(background,(0,bgY))
    screen.blit(background,(0,bgY2))
    #pygame.display.update()
    
coin=pygame.image.load('dollar.png')#<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>#
coin=pygame.transform.scale(coin,(30,30))
xcoin=random.randint(180,790)
ycoin=random.randint(-1200,-200)

def coinreward(pic,xcor,ycor):
    global coinrect
    coinrect=pic.get_rect(x=xcor,y=ycor)
    screen.blit(pic,(xcor,ycor))

bullet=pygame.image.load('bullet.png')
bullet=pygame.transform.scale(bullet,(28,28))
xbullet=0
ybullet=yaxis
xcbullet=0
ycbullet=-10
bullet_state='hold'
bulrect=bullet.get_rect(x=xbullet,y=ybullet)

def goli(image,xcor,ycor):
    global bulrect
    bulrect=image.get_rect(x=xcor+40,y=ycor+10)
    global bullet_state
    bullet_state='fire'
    screen.blit(image,(xcor+40,ycor+10))

score=0
lives=200
speed=120
bgspeed=3
carelative=3

fnt=pygame.font.Font('Orbitron-VariableFont_wght.ttf',28)
xfnt=0
yfnt=0

def stat(xcor,ycor,score,lives):
    status=fnt.render('Score: '+ str(score),True,(255,255,255))
    life=fnt.render('Health: '+ ('|'*(lives//2)),True,(255,255,255))
    screen.blit(status,(xcor,ycor))
    screen.blit(life,(xfnt,yfnt+30))
pygame.time.set_timer(USEREVENT+1,500)
a=True
while a:
    redrawWindow(bg2)
    #clock.tick(speed)
    bgY += bgspeed
    bgY2 +=bgspeed
    clock.tick(fps)

    if bullet_state is 'fire':
        goli(bullet,xbullet,ybullet)
        laserSound=pygame.mixer.Sound("laser.wav")
        laserSound.play()
        clock.sleep(0.5)   #---->is it needed?
        ybullet+=ycbullet
    if ybullet<=0:
        bullet_state='hold'
        ybullet=yaxis
    
    if bgY>=bg.get_height():
        bgY=bg.get_height()*-1
    if bgY2>=bg.get_height():
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
                xc=carelative*-1
            if event.key==pygame.K_RIGHT:
                xc=carelative
            if event.key==pygame.K_UP:
                yc=carelative*-1
            if event.key==pygame.K_DOWN:
                yc=carelative
            if event.key==pygame.K_SPACE and bullet_state=='hold':
                xbullet=xaxis
                goli(bullet, xbullet,ybullet)
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                xc=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                yc=0
    # coin_num=random.randint(1,4) torturemode
                
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
    
    car(car2,temp,xaxis,yaxis)
    for i in range(obstacle_num):
        obstacle(obs[i],xobs[i],yobs[i])
        yobs[i]+=ycobs
        if yobs[i]>1080:
            yobs[i]=positiony[i]
            xobs[i]=positionx[i]
        if yobs[i]>720:
            score+=1
            yobs[i]=positiony[i]
            xobs[i]=positionx[i]
        if pygame.Rect.colliderect(carrect,obsrect):
            lives-=1
        if pygame.Rect.colliderect(bulrect,obsrect) and bullet_state=='fire':
            yobs[i]=positiony[i]
            xobs[i]=positionx[i]
            bullet_state='hold'
            ybullet=yaxis
            bulrect=bullet.get_rect(x=xbullet,y=ybullet) #might not be needed

    coinreward(coin,xcoin,ycoin)
    ycoin+=ycobs
    if ycoin>720:
        ycoin=random.randint(-100,-20)
        xcoin=random.randint(180,790)
    elif pygame.Rect.colliderect(coinrect,carrect):
        score+=5
        ycoin=random.randint(-100,-20)
        xcoin=random.randint(180,790)
        print('add 5')

    
    if score%20==0 and score!=0:
        ycobs+=0.01
        bgspeed+=0.01
        carelative+=0.01

    
    if lives==0:
        game_over_text()
        a=False

    #print('|'*lives)
    stat(xfnt,yfnt,score,lives)
    positionx=[random.randint(180,790) for x in range(obstacle_num)]
    positiony=[random.randint(-1200,-200) for x in range(obstacle_num)]
    

    pygame.display.update()
    
pygame.quit()
