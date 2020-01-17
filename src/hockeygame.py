import sys
import pygame
import random
pygame.init()

# Initialize pygame so it runs in the background and manages things

#defining colors

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
BLUE=(0, 255, 255)


#creating puck
class Puck:
    def __init__(self, x, y):
        self.image=pygame.image.load('src/img/bluecircle.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect=self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    
    def show(self):
        screen.blit(self.image, self.rect)

    def start(self):
        self.velocity=8
        self.direction=random.randrange(-45, 45)
    
    def bounce(self, diff):
        self.direction=(180-self.direction)%360
        self.direction-=diff
        self.velocity *=1.1
    
    def checkhit(self, paddle):
        if self.rect.colliderect(Paddle.rect):
            Puck.bounce()

class Paddle:
    def __init__(self, x, y):
        self.image=pygame.image.load('src/img/blackrectangle.png')
        self.image=pygame.transform.scale(self.image, (200, 100))
        self.rect=self.image.get_rect()
        self.rect.x, self.rect.y = x,y

    def show(self):
        screen.blit(self.image, self.rect)

    def moveLeft(self, pixels):
        self.rect.x-=pixels
        if self.rect.x<0:
            self.rect.x=0
    def moveRight(self, pixels):
        self.rect.x+=pixels
        if self.rect.x>600:
            self.rect.x=600

Puck=Puck(275, 275)
PaddleA=Paddle(30, 550)
PaddleB=Paddle(200, 50)


score1=0
score2=0

carryOn=True

#clearing screen and setting up midline
screen = pygame.display.set_mode( (600, 600) )
pygame.display.set_caption("Air Hockey")
screen.fill(WHITE)
pygame.draw.line(screen, BLACK, (0, 299), (600, 299),5)
pygame.display.flip()


while carryOn==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           carryOn = False

    Puck.show()
    PaddleA.show()
    PaddleB.show()
    
    Puck.start()


    #moving paddle when the user presses arrow keys (player A) or a/d keys (player B)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        PaddleA.moveLeft(5)
    if keys[pygame.K_d]:
        PaddleA.moveRight(5)
    if keys[pygame.K_LEFT]:
        PaddleB.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        PaddleB.moveRight(5)

  
    pygame.display.flip()

