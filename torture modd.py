'''Torture Mode (beta)
This mode is still in development.
*************WARNING**************
Please play this mode at your own risk as long exposure on this mode might lead to headaches 
and could also trigger rage emotions in humans
Note: This is a modified version of Easy mode. Kindly refer to Easy mode first if you haven't, before reading this.'''
import pygame
from pygame.locals import *
import random
from pygame.constants import *
from pygame.locals import *
from pygame import mixer

pygame.init()
pygame.display.init
screen=pygame.display.set_mode([1080,720],HWSURFACE | DOUBLEBUF | RESIZABLE)
caption=pygame.display.set_caption('Delta SpeedRun')
icon=pygame.image.load('./Misc/racing.png')
pygame.display.set_icon(icon)

#background music
mixer.init()
mixer.music.load("./Music/Anxiety torture mode.mp3")
mixer.music.play(-1)

#canvas background images. bg is short for background
fps=60
clock=pygame.time.Clock()
gameoverwallpaper=pygame.image.load('./backgrounds/gameoverwallpaper.jpg')
gameoverwallpaper=pygame.transform.scale(gameoverwallpaper,(1080,720))
bg=pygame.image.load('./backgrounds/bgcompressed.jpeg')
bg2=pygame.image.load('./backgrounds/Road pic 1 filter.jpg')
bg=pygame.transform.scale(bg,(1080,720))
bg2=pygame.transform.scale(bg2,(1080,720))
bgY=0
bgY2=bg.get_height()
bgX=0
bgX2=0
mainbackground=bg

car1=pygame.image.load('./Cars/car.png')       #<div>Icons made by <a href="https://www.flaticon.com/authors/mynamepong" title="mynamepong">mynamepong</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
car2=pygame.image.load('./Cars/car2.png')      #<div>Icons made by <a href="https://www.flaticon.com/authors/berkahicon" title="berkahicon">berkahicon</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
car3=pygame.image.load('./Cars/car3.png')      #<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#<a href="https://www.vecteezy.com/free-vector/car">Car Vectors by Vecteezy</a>
#<a href="https://www.vecteezy.com/free-vector/car">Car Vectors by Vecteezy</a>

#obstacle tree <a href="https://www.vecteezy.com/free-vector/tree">Tree Vectors by Vecteezy</a>

car1=pygame.transform.scale(car1,(120,120))
car2=pygame.transform.scale(car2,(120,120))
car3=pygame.transform.scale(car3,(120,120))
temp=pygame.transform.scale(car2,(20,100))
maincar=car1
xaxis = 500
yaxis = 570
xc=0
yc=0

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
buttonretry=pygame.image.load('./buttons/buttons.png')
buttonretry2=pygame.image.load('./buttons/buttons2.png')
buttonexit=pygame.image.load('./buttons/buttonexit.png')
buttonexit2=pygame.image.load('./buttons/buttonexit2.png')

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
obs1=pygame.image.load('./Obstacles/tree1.png')
obs2=pygame.image.load('./Obstacles/tree2.png')
obs3=pygame.image.load('./Obstacles/tree3.png')
obs4=pygame.image.load('./Obstacles/tree4.png')
obs5=pygame.image.load('./Obstacles/tree5.png')
obs6=pygame.image.load('./Obstacles/cones.png')
obs7=pygame.image.load('./Obstacles/traffic-barriers.png')
obs8=pygame.image.load('./Obstacles/barrier.png')
obs9=pygame.image.load('./Obstacles/ditch.png')   
obs10=pygame.image.load('./Obstacles/obstacle-hole.png')

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
obstacle_num=random.randint(15,20)
obs=[]
xobs=[]
yobs=[]
positionx=[]
positiony=[]
ycobs=random.randint(5,7)
for i in range(obstacle_num):
    random_obstacles=random.choice(all_obstacles)
    obs.append(random_obstacles)
    xobs.append(random.randint(180,830))
    yobs.append(random.randint(-1200,-200))
    positionx.append(random.randint(180,830))
    positiony.append(random.randint(-1200,-200))

def obstacle(img,xcor,ycor):
    global obsrect
    obsrect=img.get_rect(x=xcor,y=ycor)
    screen.blit(img,(xcor,ycor))

person1=pygame.image.load('./Obstacles/person.png')
person1=pygame.transform.scale(person1,[70,70])
pson=pygame.transform.scale(person1,[70,70])
person2=pygame.image.load('./Obstacles/person2.png')
person2=pygame.transform.scale(person2,[70,70])
people=[person1,person2]
persona=random.choice(people)
xperson=180
yperson=random.randint(-2000,-200)
x_change_person=6

def personobs(img,xcor,ycor):
    global personrect
    personrect=img.get_rect(x=xcor,y=ycor)
    screen.blit(img,(xcor,ycor))


def redrawWindow(background):
    screen.blit(background,(bgX,bgY))
    screen.blit(background,(bgX2,bgY2))
    #pygame.display.update()
    
coin=pygame.image.load('./Misc/dollar.png')#<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>#
coin=pygame.transform.scale(coin,(30,30))
xcoin=random.randint(180,790)
ycoin=random.randint(-1200,-200)



def coinreward(pic,xcor,ycor):
    global coinrect
    coinrect=pic.get_rect(x=xcor,y=ycor)
    screen.blit(pic,(xcor,ycor))


bullet=pygame.image.load('./Misc/bullet.png')
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
bgspeed=5
bgXspeed=5
carelative=5

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
        mixer.music.set_volume(1)
        click=False
        redrawWindow(mainbackground)
        #clock.tick(speed)
        bgY += bgspeed
        bgY2 +=bgspeed
        bgX+=bgXspeed
        bgX2+=bgXspeed
        clock.tick(fps)

        if bullet_state is 'fire':
            goli(bullet,xbullet,ybullet)
            ybullet+=ycbullet
        if ybullet<=0:
            bullet_state='hold'
            ybullet=yaxis
        #shifting the image vertically
        if bgY>=bg.get_height():               #RESETTING BACKGROUND
            bgY=bg.get_height()*-1
        if bgY2>=bg.get_height():
            bgY2=bg.get_height()*-1
        #shifting the image horizontally
        if bgX>10:
            bgXspeed=-5
        if bgX<0:
            bgXspeed=5
        if bgX2>10:
            bgXspeed=-5
        if bgX2<0:
            bgXspeed=5
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                mainloop=False
                loop1=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    loop2=True
                    loop1=False
                if event.key==pygame.K_LEFT:
                        xc=carelative*-1
                        tyrescreechSound=pygame.mixer.Sound('./Music/tyrescreech1.mp3')
                        tyrescreechSound.set_volume(0.2)
                        tyrescreechSound.play()
                if event.key==pygame.K_RIGHT:
                    xc=carelative
                    tyrescreechSound=pygame.mixer.Sound('./Music/tyrescreech1.mp3')
                    tyrescreechSound.set_volume(0.2)
                    tyrescreechSound.play()
                if event.key==pygame.K_UP:
                    yc=carelative*-1
                if event.key==pygame.K_DOWN:
                    yc=carelative
                if event.key==pygame.K_SPACE and bullet_state=='hold':
                    xbullet=xaxis
                    goli(bullet, xbullet,ybullet)
                    laserSound=pygame.mixer.Sound("./Music/laser.wav")
                    laserSound.play()
                if event.key==pygame.K_q:
                    mainbackground=bg
                if event.key==pygame.K_w:
                    mainbackground=bg2
                if event.key==pygame.K_1:
                    maincar=car1
                if event.key==pygame.K_2:
                    maincar=car2
                if event.key==pygame.K_3:
                    maincar=car3
            
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    xc=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    yc=0
                    
        xaxis+=xc
        yaxis+=yc
        if xaxis<=180:
            xaxis=180
        if xaxis>=770:
            xaxis=770
        if yaxis<=40:
            yaxis=40
        if yaxis>=600:
            yaxis=600
        
        car(maincar,temp,xaxis,yaxis)
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
                carcrashSound=pygame.mixer.Sound('./Music/carcrash.mp3')
                carcrashSound.play()
            if pygame.Rect.colliderect(bulrect,obsrect) and bullet_state=='fire':
                explosionSound=pygame.mixer.Sound('./Music/explosion.wav')
                woodcrashSound=pygame.mixer.Sound('./Music/woodcrash.mp3')
                randomsound=random.choice([explosionSound,woodcrashSound])
                randomsound.play()
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
            coinchime=pygame.mixer.Sound('./Music/coin chime.mp3')
            coinchime.play()
            ycoin=random.randint(-100,-20)
            xcoin=random.randint(180,790)
            print('add 5')

        personobs(persona,xperson,yperson)
        yperson+=ycobs
        if xperson<900 and yperson>0:
            xperson+=x_change_person
        if pygame.Rect.colliderect(personrect,carrect):
            print('Game Over')
            loop1=False
            loop2=True
        elif yperson>3500:
            yperson=random.randint(-2000,-200)
            xperson=180

        
        if score%40==0 and score!=0:
            xs=random.uniform(0.1,0.5)
            ycobs+=random.uniform(0.1,0.5)
            bgspeed+=xs
            x_change_person+=xs
            carelative+=xs

            mainbackground=bg2
        if score%30==0 and score!=0:
            mainbackground=bg
        

        
        if lives<=0:
            loop1=False
            loop2=True

        print('|'*lives)
        stat(xfnt,yfnt,score,lives)
        positionx=[random.randint(180,790) for x in range(obstacle_num)]
        positiony=[random.randint(-1200,-200) for x in range(obstacle_num)]
        

        pygame.display.update()
    while loop2:
        mixer.music.set_volume(0.2)
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
                sound=pygame.mixer.Sound("./Music/button-3.mp3")
                sound.play()
                score=0
                lives=200
                xaxis=500
                yaxis=570
                xobs=[]
                yobs=[]
                positionx=[]
                positiony=[]
                for i in range(obstacle_num):
                    random_obstacles=random.choice(all_obstacles)
                    obs.append(random_obstacles)
                    xobs.append(random.randint(180,790))
                    yobs.append(random.randint(-1200,-200))
                    positionx.append(random.randint(180,790))
                    positiony.append(random.randint(-1200,-200))
                bgspeed=5
                ycobs=5
                yperson=random.randint(-2000,-200)
                bgX=0
                bgX2=0
                bgXspeed=5
                loop1=True
                loop2=False
        if exitrect.collidepoint(mousepos):
            exitbutton(buttonexit2,870,620)
            if pygame.mouse.get_pressed()[0]==1 and click==False:
                loop2=False
                mainloop=False

        pygame.display.update()

    
pygame.quit()
