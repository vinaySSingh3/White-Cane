import pygame,time,random,os
pygame.init()


#this is for diplaying o/p on the windows scale of 50,50
os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"



#frames per second
FPS=20
# testsound = pygame.mixer.Sound("test.wav")            #game sound
left = pygame.mixer.Sound("left.wav")
left2 = pygame.mixer.Sound("left2.wav")
left3 = pygame.mixer.Sound("left3.wav")
left4 = pygame.mixer.Sound("left4.wav")
left5 = pygame.mixer.Sound("left5.wav")

right = pygame.mixer.Sound("right.wav")
right2 = pygame.mixer.Sound("right2.wav")
right3 = pygame.mixer.Sound("right3.wav")
right4 = pygame.mixer.Sound("right4.wav")
right5 = pygame.mixer.Sound("right5.wav")


jump = pygame.mixer.Sound("jump.wav")
slide = pygame.mixer.Sound("slide.wav")

singel_left = pygame.mixer.Sound("singel_left.wav")
singel_right = pygame.mixer.Sound("singel_right.wav")

left_or_right = pygame.mixer.Sound("left_or_right.wav")
left_or_right2 = pygame.mixer.Sound("left_or_right2.wav")
left_or_right3 = pygame.mixer.Sound("left_or_right3.wav")
left_or_right4 = pygame.mixer.Sound("left_or_right4.wav")

right_or_left = pygame.mixer.Sound("right_or_left.wav")
right_or_left2 = pygame.mixer.Sound("right_or_left2.wav")
right_or_left3 = pygame.mixer.Sound("right_or_left3.wav")
right_or_left4 = pygame.mixer.Sound("right_or_left4.wav")


stay = pygame.mixer.Sound("stay.wav")

crash = pygame.mixer.Sound("crash.wav")                 #noice whe helicopter crashes with obsticals
ting =pygame.mixer.Sound("ting.wav")                    #score when reached 50+

game_is_starting = pygame.mixer.Sound("game_is_starting.wav")               #just before starting the game
heli_about_to_crash =pygame.mixer.Sound("heli_about_to_crash.wav")          #point is less than 10

crashed_and_options = pygame.mixer.Sound("crashed_and_options.wav")         #when heli die then the option which can be selected by player

which_intro = pygame.mixer.Sound("which_intro.wav")                         #option for selecting intro1() or intro2()


score_less_than_100 = pygame.mixer.Sound("score_less_than_100.wav")         #this is the comment that program make if player make score
score100 = pygame.mixer.Sound("score100.wav")                               #as per the score comment is set like amazing, awesom ,good, well played etc
score200 = pygame.mixer.Sound("score200.wav")
score300 = pygame.mixer.Sound("score300.wav")
score400 = pygame.mixer.Sound("score400.wav")
score500 = pygame.mixer.Sound("score500.wav")
score600 = pygame.mixer.Sound("score600.wav")
score800 = pygame.mixer.Sound("score800.wav")
score1000 = pygame.mixer.Sound("score1000.wav")
score1500 = pygame.mixer.Sound("score1500.wav")


pause = pygame.mixer.Sound("pause.wav")

paused = False                   #for pause event .....


armyman11 = pygame.image.load("armyman11.png")             #in intro the animation of army man 150 * 150
armyman22 = pygame.image.load("armyman22.png")
armyman33 = pygame.image.load("armyman33.png")
armyman44 = pygame.image.load("armyman44.png")


icon11 = pygame.image.load("icon.png")                  #icon of the game 
pygame.display.set_icon(icon11)

#intro
#pygame.mixer.music.load("main_intro.wav")
main_intro = pygame.mixer.Sound("main_intro.wav")           #intro1
key_intro =  pygame.mixer.Sound("key_intro.wav")            #intro2
menu_options = pygame.mixer.Sound("menu_options.wav")           #menu option 
developer_option = pygame.mixer.Sound("developer_option.wav")   #developr info vinay and raju


#ARROWs and KEYS press events
press_down = pygame.mixer.Sound("press_down.wav")           # o/p of pressed key event
press_up= pygame.mixer.Sound("press_up.wav")                #you have pressed UP KEY
press_left = pygame.mixer.Sound("press_left.wav")
press_right = pygame.mixer.Sound("press_right.wav")
press_space = pygame.mixer.Sound("press_space.wav")

move_on  = pygame.mixer.Sound("move_on.wav")                #if player have pressed all required key then game will move on to the playing...
move_on2 = pygame.mixer.Sound("move_on.wav")                #if player press space key three times
press_wrong = pygame.mixer.Sound("press_wrong.wav")         #if player press wroong key


pygame.mixer.music.load("background.wav")       #background music
pygame.mixer.music.set_volume(0.1)              #background music volume set to 10% (0.1 t0 1.0 is range) 


mylist = [right,left,jump,slide] 
                    
black = (0,0,0)             #predefind color r b g 
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


#display width and hight
dw=420
dh=700


gameDisplay = pygame.display.set_mode((dw,dh))          #VVVIMP game display
pygame.display.set_caption("WHITE CANE")                #name of the game
clock = pygame.time.Clock()

#img path imaage
path = pygame.image.load('path.png')


#vehical
plane11= pygame.image.load('plane11.png')
plane22= pygame.image.load('plane22.png')
plane33= pygame.image.load('plane33.png')
plane44= pygame.image.load('plane44.png')
plane55= pygame.image.load('plane55.png')


vehi_list =[plane11,plane22,plane33,plane44,plane55]


#pixel size is 140*170
h1=pygame.image.load('h1.png')
h2=pygame.image.load('h2.png')
h3=pygame.image.load('h3.png')
h4=pygame.image.load('h4.png')
h5=pygame.image.load('h5.png')
h6=pygame.image.load('h6.png')


heli=[h1,h2,h3,h4,h5,h6]

 

def Text_objects(text, font,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()


def message_display(text,size,pos_x,pos_y,color):
    largeText = pygame.font.Font('JOKERMAN.ttf',size)
    TextSurface,TextRect = Text_objects(text, largeText,color)
    TextRect.center=((pos_x),(pos_y))
    gameDisplay.blit(TextSurface,TextRect)
    pygame.display.update()


def stop_all():
    pygame.mixer.stop()
    #pygame.mixer.music.stop()

    
def intro1():
    stop_all()
    gameDisplay.fill(green)
    #message_display(text,size,pos_x,pos_y,color)
    message_display('WHITE CANE',33,dw/2,dh/15,red)
    message_display('game has been paused!!!!',33,dw/2,dh/6,red)
    message_display('press space key to skip',20,dw/2,dh/2,blue)
    pygame.display.update()

    
    #pygame.mixer.music.play()
    main_intro.play()

    aa=1
    aaa=1
    xx = dw*2/3 - 140
    yy = dh/2 + 40
      
    gameExit = False
    while not gameExit:
        
        #gameDisplay.fill(white)
        
        pygame.display.update()

        if aa==1:                                               #in intro the bliting the helicopter animation
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

        if aaa<=5:                                            # 2 soldieer animation....
            gameDisplay.blit(armyman11,(0,dw/2))
            gameDisplay.blit(armyman44,(dw-160,dw/2))
        if aaa<=10 and aaa>5:
            gameDisplay.blit(armyman22,(0,dw/2))
            gameDisplay.blit(armyman33,(dw-160,dw/2))
        if aaa<=15 and aaa>10:
            gameDisplay.blit(armyman33,(0,dw/2))
            gameDisplay.blit(armyman22,(dw-160,dw/2))
        if aaa<=20 and aaa>15:
            gameDisplay.blit(armyman44,(0,dw/2))
            gameDisplay.blit(armyman11,(dw-160,dw/2))
        if aaa>20:
            aaa=1
        aaa +=1
            
        
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

        pygame.display.update()
        gameDisplay.fill(green)
        #message_display('WHITE CANE',33,dw/2,dh/15,red)
        clock.tick(FPS)


def intro2():
    #pygame.mixer.music.play()
    gameDisplay.fill(white)
    message_display('WHITE CANE',33,dw/2,dh/10,red)
    message_display('we are in HURRY!!! ',20,dw/2,dh/2,blue)
    pygame.display.update()
    stop_all()
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    pygame.mixer.Sound.play(key_intro)
    gameExit = False
    while not gameExit:
        gameDisplay.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit function is running")
                pygame.quit()
                quit()

            if a>=1 and b>=1 and c>=1 and d>=1 and e>=1:
                time.sleep(3)
                stop_all()
                move_on.play()
                time.sleep(5)
                game_loop()

            if e ==3:
                time.sleep(2)
                stop_all()
                move_on2.play()
                time.sleep(4)
                game_loop()
                

            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_SPACE:
                    stop_all()
                    press_space.play()
                    message_display('you have pressed SPACE key',20,dw/2,dh/2,blue)
                    e=e+1

                elif event.key == pygame.K_UP:
                    stop_all()
                    press_up.play()
                    message_display('you have pressed UP key',20,dw/2,dh/2,blue)
                    a=a+1
                    
                elif event.key == pygame.K_DOWN:
                    stop_all()
                    press_down.play()
                    message_display('you have pressed DOWN key',20,dw/2,dh/2,blue)
                    b=b+1
                    
                elif event.key == pygame.K_LEFT:
                    stop_all()
                    press_left.play()
                    message_display('you have pressed LEFT key',20,dw/2,dh/2,blue)
                    c=c+1
                    
                elif event.key == pygame.K_RIGHT:
                    stop_all()
                    press_right.play()
                    message_display('you have pressed RIGHT key',20,dw/2,dh/2,blue)
                    d=d+1

                elif event.key != pygame.K_UP or pygame.K_LEFT or pygame.K_DOWN or pygame.K_RIGHT or pygame.K_SPACE:
                    stop_all()
                    press_wrong.play()
                    message_display('you have pressed WRONG key',20,dw/2,dh/2,blue)

                else:
                    game_loop()
                #gameDisplay.fill(white)
                pygame.display.update()
                message_display('WHITE CANE',33,dw/2,dh/10,red)
                gameDisplay.fill(white)


def vehi(vehi_x,vehi_y,i):
    vehi_choose = vehi_list[i]
    gameDisplay.blit(vehi_choose,(vehi_x,vehi_y))


def score(score):
    text = smallfont.render("Score: "+str(score), True , blue)
    gameDisplay.blit(text,[0,0])

def menu():
    stop_all()
    menu_options.play()
    gameDisplay.fill(white)
    message_display('WHITE CANE',33,dw/2,dh/10,red)
    message_display('** MENU **',20,dw/2,dh/10*2,green)
    message_display('for HOME press SPACE',20,dw/2,dh/10*3,blue)
    message_display('to play again press UP key',20,dw/2,dh/10*4,blue)
    message_display('to know about developers DOWN key',20,dw/2,dh/10*5,blue)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro()

                if event.key == pygame.K_UP:
                    game_loop()

                if event.key == pygame.K_DOWN:
                    developer()

                else:
                    menu()

def developer():
    stop_all()
    developer_option.play()
    gameDisplay.fill(white)
    message_display('WHITE CANE',33,dw/2,dh/10,red)
    message_display('** DEVELOPER **',20,dw/2,dh/10*2,green)
    message_display('VINAY SINGH',20,dw/2,dh/10*3,blue)
    message_display('RAJU SHERLA',20,dw/2,dh/10*4,blue)
    message_display('for Menu press any key',15,dw/2,dh/10*9,blue)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                menu()
    


def unpause():
    stop_all()
    global paused
    paused = False


def pausedFun():
    stop_all()
    pause.play()
    message_display('game has been paused!!!!',33,dw/2,dh/20,red)
    message_display('for RESUME press SPACE ',20,dw/2,dh/10*2,blue)
    message_display('for HOME press UP key',20,dw/2,dh/10*3,blue)
    message_display('for MENU press DOWN key',20,dw/2,dh/10*4,blue)


    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:   

                if event.key == pygame.K_UP:
                    intro1()
                    
                if event.key == pygame.K_SPACE:
                    unpause()

                if event.key == pygame.K_DOWN:
                    menu()


def game_loop():
    pygame.display.update()
    pygame.mixer.music.play()
    stop_all()
    game_is_starting.play()
    column1= False
    column2= False
    column3= False

    global paused

    life=100
    score=0
    
    x,y=0,0                         # this is for path 
    xx=140                          #this is for helicopter position width... 140 is the heli width and display is 3 times of that
    yy=dh-170                       #this is for helicopter position hight... 170 is the heli hight and display hight is 700 hence subtracted 
    aa=1                             #just for the loop for the path
    i=0
    list2=[1,2,3,4,5,6,7,8]
    list3=[1,2,3,4,5]
    list1=[10,150,290]              #list tp select the plane position from row 1 row2 or row 3
    
    list011=[150,290]               #list tp select the plane position from  row2 or row 3
    list101=[10,290]                #list tp select the plane position from  row1 or row 3
    list110=[10,150]                #list tp select the plane position from  row1 or row 2
    
    vehi_pos_x_11 = random.choice(list1)

    vehi_pos_x = vehi_pos_x_11

    
    vehi_pos_y = -200
    
    vehi_speed = 14                         #7
    
    gameExit = False
    while not gameExit:
        
        gameDisplay.blit(path,(0,0))                    #for path scrolling....
        rel_y = y % path.get_height()

        gameDisplay.blit(path,(0,rel_y - path.get_height()))
        if rel_y < dh:
            gameDisplay.blit(path,(0,rel_y))
            y=y+4

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
                if event.key == pygame.K_DOWN:          # or pygame.K_s:
                    yy +=70    
                if event.key == pygame.K_UP:            # or pygame.K_w:
                    #yy -=70
                    vehi_speed += 0.1 
                if event.key == pygame.K_LEFT:          # or pygame.K_a:
                    xx -=70
                if event.key == pygame.K_RIGHT:         # or pygame.K_d:           #have to update..../.,;'[p[]@!$#%^%*(&(^^#
                    xx +=70
                if event.key == pygame.K_SPACE:
                    if score>0:
                        paused = True
                        pausedFun()

            
        if xx>140*2:                                #the condition where heli can not go out of the display window
            xx=140*2
        if xx<0:
            xx=0
        if yy>dh-170:
            yy=dh-170

        if vehi_pos_y >dh:                          #the condition where new vehi genrated and speed is also get increase
            vehi_pos_y = -200

            if column1== False and column2== False and column3== False :
                
                vehi_pos_x_11 = random.choice(list1)
                vehi_pos_x = vehi_pos_x_11

            if column1== True :
                vehi_pos_x_11 = random.choice(list011)
                vehi_pos_x = vehi_pos_x_11

            if column2== True :
                vehi_pos_x_11 = random.choice(list101)
                vehi_pos_x = vehi_pos_x_11

            if column3== True :
                vehi_pos_x_11 = random.choice(list110)
                vehi_pos_x = vehi_pos_x_11
            

            if vehi_pos_x == 10 and vehi_pos_y <= -50:                                    #column 1111
                column1= True
                column2= False
                column3= False
                
                if xx == -70 or xx == 0 :
                    lol= random.choice(list3)
                    if lol == 1:
                        right.play()
                    if lol == 2:
                        right2.play()
                    if lol == 3:
                        right3.play()
                    if lol == 4:
                        right4.play()
                    if lol == 5:
                        right5.play()
                        
                if xx == 70 :
                    singel_right.play()
                if xx == 140 or xx == 210 or xx == 280 or xx == 350:
                    stay.play()

            if vehi_pos_x == 150 and vehi_pos_y <= -50:                                     #column 2222
                column1= False
                column2= True
                column3= False
                
                if xx == 70 :
                    singel_left.play()
                if xx == 140 :
                    lol= random.choice(list2)
                    if lol==1:
                        left_or_right.play()
                    if lol==2:
                        right_or_left.play()
                    if lol==3:
                        left_or_right2.play()
                    if lol==4:
                        right_or_left2.play()
                    if lol==5:
                        left_or_right3.play()
                    if lol==6:
                        right_or_left3.play()
                    if lol==7:
                        left_or_right4.play()
                    if lol==8:
                        right_or_left4.play()


                        
                if xx == 210 :
                    singel_right.play()

                if xx == -70 or xx == 0 or xx == 280 or xx == 350:
                    stay.play()   


            if vehi_pos_x == 290 and vehi_pos_y <= -50:                                   #column 3333
                column1= False
                column2= False
                column3= True
                
                if xx==280 or xx== 350:
                    left.play()
                if xx == 210:
                    singel_left.play()
                if xx == -70 or xx == 0 or xx == 70 or xx == 140:
                    stay.play()
                  
            vehi_speed += 0.5
            i +=1
            if i>=4:
                i=0
            if vehi_speed >= 27:
                vehi_speed = 27
                                                                                #logic for crash events:
        if   vehi_pos_y >= yy :
            
            if column1 == True and ( xx == -70 or xx == 0 or xx== 70 ):
                life -=1
                stop_all()
                crash.play()
            if column2 == True and ( xx == 70 or xx == 140 or xx == 210 ):
                life -=1
                stop_all()
                crash.play()
            if column3 == True and ( xx== 210 or xx == 280 or xx== 350 ):
                life -=1
                stop_all()
                crash.play()

        if vehi_pos_y >=yy:                         #condition to increase  the score
            score +=0.5
        #if score % 100 ==1:                         #condition to where life is increased if player cross his scoree by 100
        #    life +=2

        if life >=100:                              #if life is at 100 ie maximum then noit will stay constant
            life =100

        if score % 50 ==1:                          #ting sond for player so that he can know he is scoreing
            stop_all()
            ting.play()


        if life <0:                                            #if player loose the game
            gameDisplay.fill(white)
            stop_all()
            while True:
                message_display("Score: "+str(score),40,dw/2,dh/2,blue)

                if score > 1500 :
                    score1500.play()
                    
                elif score > 1000 :
                    score1000.play()
                    
                elif score > 800 :
                    score800.play()
                    
                elif score > 600 :
                    score600.play()
                    
                elif score > 500 :
                    score500.play()
                    
                elif score > 400 :
                    score400.play()
                    
                elif score> 300 :
                    score300.play()
                    
                elif score >200 :
                    score200.play()
                    
                elif score >=100 :
                    score100.play()
                    
                else :
                    score_less_than_100.play()

                time.sleep(6)
                event_of_crash()

            
        #message_display(text,size,pos_x,pos_y,color)
        message_display("life: "+str(life),20,55,25,red)   
        message_display("Score: "+str(score),20,340,25,blue)
        pygame.display.flip()
        clock.tick(FPS)

def event_of_crash():                                           #the event where player can choose what to do if he looses the game
    gameDisplay.fill(white)
    message_display('good game player!!!!',33,dw/2,dh/20,red)
    message_display('for play again press UP key ',20,dw/2,dh/10*2,blue)
    message_display('for QUIT press key DOWN key',20,dw/2,dh/10*3,blue)
    message_display('for INTRO press LEFT key',20,dw/2,dh/10*4,blue)
    stop_all()
    crashed_and_options.play()

    something = False

    while not something:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit function is running")
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                    
                if event.key ==  pygame.K_UP:
                    game_loop()

                elif event.key == pygame.K_DOWN:
                    stop_all()
                    pygame.quit()
                    quit() 

                elif event.key == pygame.K_LEFT:
                    intro1()

                else:
                    event_of_crash()


intro1()
intro2()
game_loop()
pygame.quit()
quit()
#score life
#crash event rakhna h
#life 3 set karni h and upar wale bhag main jaha first time plane genrate hota h waha aisa condition dalna h
#ki jab vo crash bhi ho to count na kare fir baki time kare to no problem aisa kuch

#sab ko folder main shift karna h
#intro 1 plus intro 2 update karna h thoda visual dalna h dalna h




#aur kya karna h  bhai add karna h hard aur easy nahhhhhh nhi karna not needed
#intro 2 par kaam karna h 
#pata nhi kyun pause event main problem aa raha h jab intro 2 se game main jate h dfhsfsf
#intrto 2 main description bhi daalna h ki event press par kya hona chahiye matlab key ka use kya h



#intro2 main aisa bhi kiya ja sakta h ki space key preessedsd 1time 2end time 3td time jab time ho tab ye karna


#quit option bhi dalna h game main....sab menu main,.,.,.,.,.,,.,.,.,,.c
