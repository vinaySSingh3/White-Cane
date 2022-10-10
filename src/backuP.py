import pygame,time,random,os
pygame.init()


#this is for diplaying o/p on the windows scale of 50,50
os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

#frames per second
FPS=20

# testsound = pygame.mixer.Sound("test.wav")
left = pygame.mixer.Sound("left.wav")
right = pygame.mixer.Sound("right.wav")
jump = pygame.mixer.Sound("jump.wav")
slide = pygame.mixer.Sound("slide.wav")

#intro
pygame.mixer.music.load("main_intro.wav")
#main_intro = pygame.mixer.Sound("main_intro.wav")
main_intro1 = pygame.mixer.Sound("main_intro1.wav")
main_intro2 = pygame.mixer.Sound("main_intro2.wav")
key_intro =  pygame.mixer.Sound("key_intro.wav")


#ARROWs and KEYS press events
press_down = pygame.mixer.Sound("press_down.wav")
press_up= pygame.mixer.Sound("press_up.wav")
press_left = pygame.mixer.Sound("press_left.wav")
press_right = pygame.mixer.Sound("press_right.wav")

move_on = pygame.mixer.Sound("move_on.wav")                                        
press_wrong = pygame.mixer.Sound("press_wrong.wav")

#pygame.mixer.music.load("test.wav")             #to load big file
#pygame.mixer.music.load("intro5sec.wav")        #1st intro part
#pygame.mixer.music.load("main intro.wav")       #2end intro part


mylist = [right,left,jump,slide] 

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#display width and high
dw=414
dh=700

gameDisplay = pygame.display.set_mode((dw,dh))
pygame.display.set_caption("run run")
clock = pygame.time.Clock()

#img
vin = pygame.image.load('vin.jpg')
path = pygame.image.load('path.png')

#vehical
plane11= pygame.image.load('plane11.png')
plane22= pygame.image.load('plane22.png')
plane33= pygame.image.load('plane33.png')
plane44= pygame.image.load('plane44.png')
plane55= pygame.image.load('plane55.png')

vehi_list =[plane11,plane22,plane33,plane44,plane55]



#pixel size is 138*170
h1=pygame.image.load('h1.png')
h2=pygame.image.load('h2.png')
h3=pygame.image.load('h3.png')
h4=pygame.image.load('h4.png')
h5=pygame.image.load('h5.png')
h6=pygame.image.load('h6.png')
heli=[h1,h2,h3,h4,h5,h6]
#def of fly logic 

def Text_objects(text, font):
    textSurface = font.render(text,True,blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('JOKERMAN.ttf',20)
    TextSurface,TextRect = Text_objects(text, largeText)
    TextRect.center=((dw/2),(dh/2))
    gameDisplay.blit(TextSurface,TextRect)
    pygame.display.update()
    
def intro1():
    gameDisplay.fill(red)
    message_display('press space key to skip')
    pygame.display.update()
    clock.tick(60)
    pygame.mixer.music.play()
      
    gameExit = False
    while not gameExit:
        #gameDisplay.fill(white)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit function has run")
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("event")
                    intro2()
                    gameExit= True
                else:
                    intro2()

def stop_all():
    pygame.mixer.stop()
    pygame.mixer.music.stop()

def intro2():
    stop_all()
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    pygame.mixer.Sound.play(key_intro)
    gameExit = False
    while not gameExit:
        gameDisplay.fill(white)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit function is running")
                pygame.quit()
                quit()

            if a>=1 and b>=1 and c>=1 and d>=1:
                    print('truewefhweiufhwikh')
                    time.sleep(3)
                    stop_all()
                    move_on.play()
                    time.sleep(5)
                    game_loop()

            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_SPACE:
                    print("event")
                    game_loop()
                    gameExit= True

                elif event.key == pygame.K_UP:
                    stop_all()
                    press_up.play()
                    a=a+1
                    print("a",a)

                elif event.key == pygame.K_DOWN:
                    stop_all()
                    press_down.play()
                    b=b+1
                    print("b",b)

                elif event.key == pygame.K_LEFT:
                    stop_all()
                    press_right.play()
                    c=c+1
                    print("c",c)
                    
                elif event.key == pygame.K_RIGHT:
                    stop_all()
                    press_left.play()
                    d=d+1
                    print("d",d)

                elif event.key != pygame.K_UP or pygame.K_LEFT or pygame.K_DOWN or pygame.K_RIGHT or pygame.K_SPACE:
                    stop_all()
                    press_wrong.play()

                else:
                    game_loop()



def vehi(vehi_x,vehi_y,i):

    vehi_choose = vehi_list[i]
    gameDisplay.blit(vehi_choose,(vehi_x,vehi_y))





def game_loop():
    stop_all()
    
    x,y=0,0                         # this is for path 
    xx=138                          #this is for helicopter position width... 140 is the heli width and display is 3 times of that
    yy=dh-170                       #this is for helicopter position hight... 170 is the heli hight and display hight is 700 hence subtracted 
    aa=1                             #just for the loop for the path
    i=0
    vehi_pos_x = random.randrange(0,dw-100)
    vehi_pos_y = -500

    vehi_speed = 21                         #7

    gameExit = False
    while not gameExit:
        
        gameDisplay.blit(path,(0,0))                    #for path scrolling....
        rel_y = y % path.get_height()

        gameDisplay.blit(path,(0,rel_y - path.get_height()))
        if rel_y < dh:
            gameDisplay.blit(path,(0,rel_y))
            y=y+4


        
        #vehi(vehiX,vehiy,vehiW,vehiH)
        vehi(vehi_pos_x,vehi_pos_y,i)
        vehi_pos_y += vehi_speed


        
        
        if aa==1:
            gameDisplay.blit(h1,(xx,yy))
        if aa==2:
            gameDisplay.blit(h2,(xx,yy))  
        if aa==3:
            gameDisplay.blit(h3,(xx,yy))
        if aa==4:
            gameDisplay.blit(h4,(xx,yy))
        if aa==5:
            gameDisplay.blit(h5,(xx,yy))
        if aa==6:
            gameDisplay.blit(h6,(xx,yy))
            aa=1;
        aa +=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:      # or pygame.K_s:
                    yy +=46    
                if event.key == pygame.K_UP:        # or pygame.K_w:
                    yy -=46
                if event.key == pygame.K_LEFT:      # or pygame.K_a:
                    xx -=46
                if event.key == pygame.K_d:         # or pygame.K_d:           #have to update..../.,;'[p[]@!$#%^%*(&(^^#
                    xx +=46
        if xx>138*2:                                #the condition where heli can not go out of the display window
            xx=138*2
        if xx<0:
            xx=0

        if vehi_pos_y >dh:                          #the condition where new vehi genrated and speed is also get increase
            vehi_pos_y = -200
            vehi_pos_x = random.randrange(0,dw-100) 
            vehi_speed += 0.5
            i +=1
            if i>=4:
                i=0

        # if condition where i have to put condition of colision

        
        pygame.display.flip()
        clock.tick(FPS)    
#intro1()
#intro2()
game_loop()
pygame.quit()
quit()
