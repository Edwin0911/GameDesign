import pygame
from pygame.locals import *
import random
import time

pygame.init()
width = 480
height = 360
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Whac-a-Mole")

pygame.mixer.init()
pygame.mixer.music.load("BGM.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1,0)

hamster0 = pygame.image.load('hamster_hide.png')
hamster1 = pygame.image.load('hamster_show.png')
hamster2 = pygame.image.load('star.png')

font1 = pygame.font.SysFont('SimHei', 24)
font2 = pygame.font.SysFont('SimHei', 100)  
def print_text(screen, x, y, font, text, fcolor ):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))

class Hamster():
    def __init__(self,x,y,w,h,image0,image1,image2):
        self.images = [image0,image1,image2]
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.status = random.randint(0,1)        
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
    def show(self):
        self.status = 1       
    def hide(self):
        self.status= 0
    def hit(self):
        self.status= 2
    def draw(self):
        screen.blit(self.images[self.status],(self.x,self.y))
    def collide(self,hammer):

        return self.rect.colliderect(hammer.rect) and self.status == 1
        
 
hammer0 = pygame.image.load('hammer_unknock.png')
hammer1 = pygame.image.load('hammer_knock.png')

class Hammer():
    def __init__(self,x,y,w,h,image0,image1):
        self.images = [image0,image1]
        self.x = x
        self.y = y
        self.w = int(w/2)             
        self.h = int(h/2)             
        self.status = 0          
         
    def setpos(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)   
    def switch(self,no):
        self.status = no
    def draw(self):
        screen.blit(self.images[self.status],(self.x,self.y))
        

hammer = Hammer(0,0,80,80,hammer0,hammer1)

basket =[Hamster(100,20,80,80,hamster0,hamster1,hamster2),Hamster(200,20,80,80,hamster0,hamster1,hamster2),Hamster(300,20,80,80,hamster0,hamster1,hamster2),
         Hamster(100,120,80,80,hamster0,hamster1,hamster2),Hamster(200,120,80,80,hamster0,hamster1,hamster2),Hamster(300,120,80,80,hamster0,hamster1,hamster2),
         Hamster(100,220,80,80,hamster0,hamster1,hamster2),Hamster(200,220,80,80,hamster0,hamster1,hamster2),Hamster(300,220,80,80,hamster0,hamster1,hamster2)]
                                                                             


cover_image = pygame.image.load("cover.png")
background_image = pygame.image.load("background.png")
level_image = pygame.image.load("level.png")
star = pygame.image.load("star.png")

while True:
    end_loop = False
    while not end_loop:
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
            if event.type==MOUSEBUTTONUP:
                end_loop = True
                
        screen.blit(cover_image,(0,0))
        pygame.display.update()

    end_loop2 = False
    while not end_loop2:

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONUP:
                if 190 < pygame.mouse.get_pos()[0] < 300 and 150 < pygame.mouse.get_pos()[1] < 190 :
                    select_time = 60
                    end_loop2 = True
                if 190 < pygame.mouse.get_pos()[0] < 300 and 190 < pygame.mouse.get_pos()[1] < 250:
                    select_time = 120
                    end_loop2 = True
                if 190 < pygame.mouse.get_pos()[0] < 300 and 250 < pygame.mouse.get_pos()[1] < 300:
                    select_time = 180
                    end_loop2 = True
                    
        screen.blit(level_image,(0,0))
        pygame.display.update()
        
    tStart = time.time()
    clock = pygame.time.Clock()
    score = 0 
    hit=False
    end = False
    while not end:
            
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
            if event.type==MOUSEBUTTONDOWN:
                hit=True
            if event.type==MOUSEBUTTONUP:
                hit=False
            
            
             
            
        
        screen.blit(background_image,(0,0))

        mpos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        hammer.setpos(mpos[0],mpos[1])   #set mouse position

        print_text(screen, 370, 340, font1, f'Score: {score}', (255,255,255) )
        tEnd = time.time()-tStart
        tGameover = int(select_time-tEnd)
        if tGameover<0:
            screen.blit(background_image,(0,0))
            print_text(screen, 60, 130, font2, 'YOU LOSE!', (255,255,255) )
            end = True
            pygame.display.update()
            time.sleep(5)
            
        else:    
            print_text(screen, 20, 340, font1, f'Time: {tGameover}', (255,255,255) )
            for hamster in basket:
                if random.randint(0,100)==0:    #maintain
                        
                    if random.randint(0,1000)>600:    #hide or show
                        hamster.show()
                    else:
                        hamster.hide()
                hamster.draw()
                if hamster.status == 2:
                    hamster.hide()
                if hit == True:            
                    hammer.switch(1)
                    if  hamster.collide(hammer):
                        hamster.hit()
                        score = score+10
                        if score == 1000:
                            screen.blit(background_image,(0,0))
                            print_text(screen, 80, 130, font2, 'YOU WIN!', (255,255,255) )
                            end = True
                            pygame.display.update()
                            time.sleep(5)
                            break

                else:
                    hammer.switch(0)
            hammer.draw()
        
        pygame.display.update()
        clock.tick(60)

   
