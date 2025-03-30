import pygame
import os
import random
img_path = os.path.join("C:/Users/Ajit/OneDrive/Documents/python/car race project/car.png")
car_p=pygame.image.load("C:/Users/Ajit/OneDrive/Documents/python/car race project/car.png")
WIDTH,HEIGTH=700,900
win=pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("CAR RACING GAME")

screen=pygame.transform.scale(pygame.image.load("car race project/race car sceen.png"),(WIDTH,HEIGTH))
road=pygame.transform.scale(pygame.image.load("C:/Users/Ajit/OneDrive/Documents/python/car race project/road_bg.png"),(WIDTH,HEIGTH))
road=pygame.transform.scale(pygame.image.load("car race project/road_bg_2.png"),(WIDTH,HEIGTH))
#gaME setting
gameOver=False
score=0
play=pygame.image.load("car race project/button_1.PNG").convert_alpha()
leave=pygame.image.load("car race project/button_2.PNG")
change_player=pygame.image.load("car race project/button_3.png").convert_alpha()

#Enemy
enemy_image=pygame.image.load("C:/Users/Ajit/OneDrive/Documents/python/car race project/enemy_race_car.png")
enemy_image=pygame.transform.rotate(enemy_image,180)

enemy_image_3=pygame.image.load("car race project/car_2.png")
enemy_image_3=pygame.transform.rotate(enemy_image_3,180)

enemy_image_2=pygame.image.load("car race project/race_car.png")
enemy_image_2=pygame.transform.rotate(enemy_image_2,180)

def enemy(x,y):
    win.blit(enemy_image,(x,y))

def enemy_2(x,y):
    win.blit(enemy_image_2,(x,y))  

def enemy_3(x,y):
    win.blit(enemy_image_3,(x,y))
#movment of body of enemy
#e_x=220

e_y=-20
e_y_2=-20
change_y=12

e_y_3=-20
e_y_2=-20
change_y_3=10
change_x_3=random.randint(47,590)
change_x=random.randint(47,590)
change_y_2=7
change_x_2=random.randint(47,590)
e_x=change_x
e_x_2=change_x_2  
e_x_3=change_x_3  

#COLOUR:
white=255,255,255
black=0,0,0
blue=0,0,255
r_c=71,71,71
    

#key move
class Car(object):  
    def __init__(self):
        """ The constructor of the class """
        self.imag =pygame.image.load(img_path)
        # the bird's position
        self.x = 310
        self.y = 780
        
    def handle_keys(self):       
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 10 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_s]or key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_w]or key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_d]or key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_a]or key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.imag, (self.x, self.y))
        #collision
    def collision(self):
        if self.x>590:
            self.x=589
        elif self.x<47:
            self.x=46
        elif self.y>800:
            self.y=797
        elif self.y<1:
            self.y=2

    
    


#game loop
clock=pygame.time.Clock()
fps=100*10^10000

car=Car()
road_y=0
run=True
start=False
running=False

self_y=780
self_x=310
#animtion
#menu loop _________________________
pygame.mouse.set_visible(True)
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False
    mouse_pos=pygame.mouse.get_pos() 

    win.blit(play,(200,200))
    win.blit(leave,(200,500))
    win.blit(change_player,(200,350))

    but_e=leave.get_rect()
    but_e.topleft=200,500
    #EXIT    +++++++
    if but_e.collidepoint(mouse_pos):
        pygame.draw.rect(win,(white),but_e,4)
        if pygame.mouse.get_pressed()[0]==1:
            pygame.quit()
    #CGHANGE
    but_c=change_player.get_rect()
    but_c.topleft=200,350    
    if but_c.collidepoint(mouse_pos):
        pygame.draw.rect(win,(white),but_c,4)
        if pygame.mouse.get_pressed()[0]==1:
            run=False
            start=True
            while start:
             for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                    pygame.quit()
                    start=False

                 win.blit(car_p,(200,250))
            
                 pygame.display.update()
                 win.fill(blue)
            



    but_p=play.get_rect()
    but_p.topleft=200,200
    #PLATY________________
    if but_p.collidepoint(mouse_pos):
        pygame.draw.rect(win,(white),but_p,4)
        if pygame.mouse.get_pressed()[0]==1:
            run=False
            running=True
            #main game __________________   
            while running:
             clock.tick(fps)

             for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                     pygame.quit()
                     running=False

    




             key = pygame.key.get_pressed()
             dist = 10 # distance moved in 1 frame, try changing it to 5
             if key[pygame.K_s]or key[pygame.K_DOWN]: # down key
                 self_y += dist # move down
             elif key[pygame.K_w]or key[pygame.K_UP]: # up key
                 self_y -= dist # move up
             if key[pygame.K_d]or key[pygame.K_RIGHT]: # right key
                 self_x += dist # move right
             elif key[pygame.K_a]or key[pygame.K_LEFT]: # left key
                 self_x -= dist # move l'
             elif self_x>=590:
                 self_x=589
             elif self_x<=47:
                 self_x=48
             elif self_y>800:
                 self_y=797
             elif self_y<1:
                 self_y=2


    

     #animation of moving
             road_x=0
             road_y=road_y
             road_y+=10
             win.blit(road,(road_x,road_y))
             if road_y>50:
                 road_y=10



#collision in player
    
             box=pygame.Rect(e_x,e_y,55,120)
             pygame.draw.rect(win,(r_c),box,1)
    
             box_2=pygame.Rect(self_x,self_y,55,119)
             pygame.draw.rect(win,(r_c),box_2,1)

             em=pygame.Rect(e_x_2,e_y_2,52,110)
             pygame.draw.rect(win,(r_c),em,1)

             em_2=pygame.Rect(e_x_3,e_y_3,52,110)
             pygame.draw.rect(win,(r_c),em,1)             

             if box_2.colliderect(box):
                 e_y_2=0
                 e_y_3=0
                 e_y=0
                 running=gameOver
                 run=True
             if box_2.colliderect(em):
                 e_y_2=0
                 e_y_3=0
                 e_y=0
                 running=gameOver
                 run=True
             if box_2.colliderect(em_2):
                 running=gameOver
                 run=True
        #win.fill(r_c)

             if em.colliderect(box):
                 change_x_2=random.randint(47,590)
                 change_y_2=10
             if em_2.colliderect(box_2):
                 change_x_3=random.randint(47,590)
                 change_y_3=10
             if em_2.colliderect(em):
                 change_x_2=random.randint(47,590)
                 change_y_2=10
                 






    
             if e_y>900:
                e_y=0
                change_x=random.randint(47,590)
             if em.colliderect(box):
                 change_x_2=random.randint(47,590)
             if e_y_2>900:
                e_y_2=0
                change_x_2=random.randint(47,590)


             if em_2.colliderect(box):
                 change_x_3=random.randint(40,570)
             if e_y_3>900:
                e_y_3=0
                change_x_3=random.randint(46,580)
    
    
             e_y+=change_y 
             e_y_2+=change_y_2
             e_y_3+=change_y_3

    
             e_x=change_x
             e_x_2=change_x_2
             e_x_3=change_x_3

             enemy(e_x,e_y)
             enemy_2(e_x_2,e_y_2)
             enemy_3(e_x_3,e_y_3)







             car.handle_keys()
             car.collision()
             car.draw(win) 
   

             pygame.display.update()
             win.blit(road,(0,0))
    
         
            

            

    pygame.display.update()
    win.blit(screen,(0,0))
  




       







