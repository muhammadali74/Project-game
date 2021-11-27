'''Easy mode. 
One of the three difficulty level of the game. 
The other two difficulty levels are the modified versions of this mode.
For understanding the code. Refer to this file first before reading the other two mode files'''
import pygame
from pygame.locals import *
import time
import os
import sys
import random
from pygame.constants import *
from pygame.locals import *
from pygame import mixer

#initializing pygame, setting bar ucon, caption and initializing screen canvas
pygame.init()
pygame.display.init
screen=pygame.display.set_mode([1080,720],HWSURFACE | DOUBLEBUF | RESIZABLE)
caption=pygame.display.set_caption('Delta SpeedRun')
icon=pygame.image.load('racing.png')
pygame.display.set_icon(icon)

#background music
mixer.init()
mixer.music.load("intromusic.mp3")
mixer.music.play(-1)

#canvas background images. bg is short for background
fps=60
clock=pygame.time.Clock()
gameoverwallpaper=pygame.image.load('gameoverwallpaper.jpg')
gameoverwallpaper=pygame.transform.scale(gameoverwallpaper,(1080,720))
bg=pygame.image.load('bgcompressed.jpeg')  #Downlaoded from a copyright free source. 
bg2=pygame.image.load('Road pic 1 filter.jpg')
bg=pygame.transform.scale(bg,(1080,720))
bg2=pygame.transform.scale(bg2,(1080,720))
bgY=0
bgY2=bg.get_height()
mainbackground=bg

#function for updating two images simutaneously on the screen to create a scroll bg effect.
def redrawWindow(background):
    screen.blit(background,(0,bgY))
    screen.blit(background,(0,bgY2))
    #pygame.display.update()


car1=pygame.image.load('car.png')       #<div>Icons made by <a href="https://www.flaticon.com/authors/mynamepong" title="mynamepong">mynamepong</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
car2=pygame.image.load('car2.png')      #<div>Icons made by <a href="https://www.flaticon.com/authors/berkahicon" title="berkahicon">berkahicon</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
car3=pygame.image.load('car3.png')      #<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#<a href="https://www.vecteezy.com/free-vector/car">Car Vectors by Vecteezy</a>
#<a href="https://www.vecteezy.com/free-vector/car">Car Vectors by Vecteezy</a>


#loading car images and setting initial car cordinates
car1=pygame.transform.scale(car1,(120,120))
car2=pygame.transform.scale(car2,(120,120))
car3=pygame.transform.scale(car3,(120,120))
temp=pygame.transform.scale(car2,(20,100))
maincar=car1
xaxis = 500
yaxis = 570
x_change=0
y_change=0

#function for blitting car on screen and storing car's rectangular cordinates in a variable for collission detection
def car(pic,pictemp,xcor,ycor):
    global carrect
    temp=pygame.transform.scale(pictemp,(40,70))
    carrect=temp.get_rect(x=xcor+50,y=ycor)
    screen.blit(pic,(xcor,ycor))

#loading font styles and sizes to be used in various places
fnt=pygame.font.Font('Orbitron-VariableFont_wght.ttf',28)
font=pygame.font.Font('Orbitron-VariableFont_wght.ttf',35)
font2=pygame.font.Font('Orbitron-VariableFont_wght.ttf',50)
xfnt=0
yfnt=0

#function for text when game ends
def game_over_text():
    over_text =font2.render("GAME OVER", True, (245, 255, 250))
    score_text=font.render("score:   "+str(score), True, (245, 255, 250))
    screen.blit(over_text, (200,300))
    screen.blit(score_text, (200, 450))

#loading button images
buttonretry=pygame.image.load('buttons.png')
buttonretry2=pygame.image.load('buttons2.png')
buttonexit=pygame.image.load('buttonexit.png')
buttonexit2=pygame.image.load('buttonexit2.png')

buttonretry=pygame.transform.scale(buttonretry,(190,69))
buttonretry2=pygame.transform.scale(buttonretry2,(190,69))
buttonexit=pygame.transform.scale(buttonexit,(190,69))
buttonexit2=pygame.transform.scale(buttonexit2,(190,69))

def retrybutton(img,xcor,ycor):
    global buttonrect
    buttonrect=img.get_rect(x=xcor,y=ycor)
    screen.blit(img,(xcor,ycor))

def exitbutton(img,xcor,ycor):
    global exitrect
    exitrect=img.get_rect(x=xcor,y=ycor)
    screen.blit(img,(xcor,ycor))

#loading obstacles images. obs is short for obstacles
obs1=pygame.image.load('tree1.png') #obstacle tree <a href="https://www.vecteezy.com/free-vector/tree">Tree Vectors by Vecteezy</a>
obs2=pygame.image.load('tree2.png')
obs3=pygame.image.load('tree3.png')
obs4=pygame.image.load('tree4.png')
obs5=pygame.image.load('tree5.png')
obs6=pygame.image.load('cones.png')
obs7=pygame.image.load('traffic-barriers.png') #Source: flaticon.com
obs8=pygame.image.load('barrier.png')   #Source: flaticon.com
obs9=pygame.image.load('ditch.png') #Source: flaticon.com
obs10=pygame.image.load('obstacle-hole.png')    #Source: flaticon.com

#resizing obstacles
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

#making list of all obstacles, obstacle's x,y cordinates inorder to call them randomly during game at random cordinates
all_obstacles=[obs1,obs2,obs3,obs4,obs5,obs6,obs7,obs8,obs9,obs10]
random_obstacles=random.choice(all_obstacles)
obstacle_num=random.randint(8,10)
obs=[]
x_obstacle=[]
y_obstacle=[]
random_positionx=[]
random_positiony=[]
# yc stands for Y Change
y_change_obstacle=3
for i in range(obstacle_num):
    random_obstacles=random.choice(all_obstacles)
    obs.append(random_obstacles)
    x_obstacle.append(random.randint(180,790))
    y_obstacle.append(random.randint(-1200,-200))
    random_positionx.append(random.randint(180,790))
    random_positiony.append(random.randint(-1200,-200))

#blitting obstacles on screen and getting its cordinates for collission detection
def obstacle(img,xcor,ycor):
    global obsrect
    obsrect=img.get_rect(x=xcor,y=ycor)
    screen.blit(img,(xcor,ycor))

#loading coin reward image and setting its random cordinates
coin=pygame.image.load('dollar.png')#<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>#
coin=pygame.transform.scale(coin,(30,30))
xcoin=random.randint(180,790)
ycoin=random.randint(-1200,-200)

#blitting coins on screen and getting its cordinates for collission detection
def coinreward(pic,xcor,ycor):
    global coinrect
    coinrect=pic.get_rect(x=xcor,y=ycor)
    screen.blit(pic,(xcor,ycor))

#loading bullet image and setting its initial cordinates, and state.
bullet=pygame.image.load('bullet.png') #source: flaticon.com
bullet=pygame.transform.scale(bullet,(28,28))
x_bullet=0
y_bullet=yaxis
#xc means x change
#yc means y change
x_change_bullet=0
y_change_bullet=-10
bullet_state='hold'
bulrect=bullet.get_rect(x=x_bullet,y=y_bullet)

#function for blitting bullet on screen and getting its cordinates.
def gun(image,xcor,ycor):
    global bulrect
    bulrect=image.get_rect(x=xcor+40,y=ycor+10)
    global bullet_state
    bullet_state='fire'
    screen.blit(image,(xcor+40,ycor+10))

#variables to store some important game quantities
score=0
lives=200
bgspeed=3
carelative=3


#function for displaying current stats (score, car health) on screen
def stat(xcor,ycor,score,lives):
    status=fnt.render('Score: '+ str(score),True,(255,255,255))
    life=fnt.render('Health: '+ ('|'*(lives//2)),True,(255,255,255))
    screen.blit(status,(xcor,ycor))
    screen.blit(life,(xfnt,yfnt+30))
# pygame.time.set_timer(USEREVENT+1,500)

#boolean variables needed for maintaning flow of game
loop1=True
mainloop=True
loop2=True
while mainloop:
    while loop1:
        mixer.music.set_volume(0.1)
        click=False
        redrawWindow(mainbackground)
        #to scroll background we need to constantly change its cordinates
        bgY += bgspeed
        bgY2 +=bgspeed
        clock.tick(fps)

        if bullet_state == 'fire':
            gun(bullet,x_bullet,y_bullet)
            y_bullet+=y_change_bullet
        if y_bullet<=0:
            bullet_state='hold'
            y_bullet=yaxis
        #for slide one background image just afetr the other so that it creates a continouos movement effect
        if bgY>=bg.get_height():
            bgY=bg.get_height()*-1
        if bgY2>=bg.get_height():
            bgY2=bg.get_height()*-1

        #detecting several events during game including key presses and executing instructions accordingly
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                mainloop=False
                loop1=False
            # if event.type==USEREVENT+1:
            #     speed +=5
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    loop2=True
                    loop1=False
                if event.key==pygame.K_LEFT:
                    x_change=carelative*-1
                    tyrescreechSound=pygame.mixer.Sound('tyrescreech1.mp3')
                    tyrescreechSound.set_volume(0.2)
                    tyrescreechSound.play()
                if event.key==pygame.K_RIGHT:
                    x_change=carelative
                    tyrescreechSound=pygame.mixer.Sound('tyrescreech1.mp3')
                    tyrescreechSound.set_volume(0.2)
                    tyrescreechSound.play()
                if event.key==pygame.K_UP:
                    y_change=carelative*-1
                if event.key==pygame.K_DOWN:
                    y_change=carelative
                if event.key==pygame.K_SPACE and bullet_state=='hold':
                    x_bullet=xaxis
                    gun(bullet, x_bullet,y_bullet)
                    laserSound=pygame.mixer.Sound("laser.wav")
                    laserSound.play()
                if event.key==pygame.K_1:
                    mainbackground=bg
                if event.key==pygame.K_2:
                    mainbackground=bg2
                if event.key==pygame.K_3:
                    pass
                if event.key==pygame.K_4:
                    pass
                if event.key==pygame.K_q:
                    maincar=car1
                if event.key==pygame.K_w:
                    maincar=car2
                if event.key==pygame.K_e:
                    maincar=car3
            
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    y_change=0

        #changing cordinates of car as per user's input            
        xaxis+=x_change
        yaxis+=y_change
        #restrcting car to remain within the boundaries
        if xaxis<=180:
            xaxis=180
        if xaxis>=790:
            xaxis=790
        if yaxis<=40:
            yaxis=40
        if yaxis>=600:
            yaxis=600
        
        car(maincar,temp,xaxis,yaxis)
        #for displaying, manipulating obstacles at random positions after random time
        for i in range(obstacle_num):
            obstacle(obs[i],x_obstacle[i],y_obstacle[i])
            y_obstacle[i]+=y_change_obstacle
            if y_obstacle[i]>1080:
                y_obstacle[i]=random_positiony[i]
                x_obstacle[i]=random_positionx[i]
            if y_obstacle[i]>720:
                score+=1
                y_obstacle[i]=random_positiony[i]
                x_obstacle[i]=random_positionx[i]
            #for detecting collision between car and obstacle
            if pygame.Rect.colliderect(carrect,obsrect):
                lives-=1
                carcrashSound=pygame.mixer.Sound('carcrash.mp3')
                carcrashSound.play()
            #for detecting collision between bullet and obstacle
            if pygame.Rect.colliderect(bulrect,obsrect) and bullet_state=='fire':
                explosionSound=pygame.mixer.Sound('explosion.wav')
                woodcrashSound=pygame.mixer.Sound('woodcrash.mp3')
                randomsound=random.choice([explosionSound,woodcrashSound])
                randomsound.play()
                y_obstacle[i]=random_positiony[i]
                x_obstacle[i]=random_positionx[i]
                bullet_state='hold'
                y_bullet=yaxis
                score+=1
                bulrect=bullet.get_rect(x=x_bullet,y=y_bullet) #might not be needed

        coinreward(coin,xcoin,ycoin)
        ycoin+=y_change_obstacle
        if ycoin>720:
            ycoin=random.randint(-100,-20)
            xcoin=random.randint(180,790)
        #for detecting collision between car and coin
        elif pygame.Rect.colliderect(coinrect,carrect):
            score+=5
            coinchime=pygame.mixer.Sound('coin chime.mp3')
            coinchime.play()
            ycoin=random.randint(-100,-20)
            xcoin=random.randint(180,790)
            print('add 5')

        #for increasing game speed after user reaches a threshlod value
        if score%20==0 and score!=0:
            y_change_obstacle+=0.01
            bgspeed+=0.01
            carelative+=0.01

        # exit if health is zero
        if lives<=0:
            loop1=False
            loop2=True
        #print('|'*lives)
        stat(xfnt,yfnt,score,lives)
        #assigning new random positions to obstacles
        random_positionx=[random.randint(180,790) for x in range(obstacle_num)]
        random_positiony=[random.randint(-1200,-200) for x in range(obstacle_num)]
        

        pygame.display.update()
    
    while loop2:
        mixer.music.set_volume(0.6)
        click=False
        screen.blit(gameoverwallpaper,(0,0))
        game_over_text()
        retrybutton(buttonretry,870,520)
        exitbutton(buttonexit,870,620)
        #get the mouse pointer position
        mousepos=pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                loop2=False
                mainloop=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    loop2=False
                    mainloop=False
        #for checking if mouse hover and/or clicks the button image
        if buttonrect.collidepoint(mousepos):
            retrybutton(buttonretry2,870,520)
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                #resetting game settings
                score=0
                lives=200
                xaxis=500
                yaxis=570
                x_obstacle=[]
                y_obstacle=[]
                random_positionx=[]
                random_positiony=[]
                for i in range(obstacle_num):
                    random_obstacles=random.choice(all_obstacles)
                    obs.append(random_obstacles)
                    x_obstacle.append(random.randint(180,790))
                    y_obstacle.append(random.randint(-1200,-200))
                    random_positionx.append(random.randint(180,790))
                    random_positiony.append(random.randint(-1200,-200))
                bgspeed=3
                y_change_obstacle=3
                loop1=True
                loop2=False
        if exitrect.collidepoint(mousepos):
            exitbutton(buttonexit2,870,620)
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                loop2=False
                mainloop=False

        pygame.display.update()


    
pygame.quit()