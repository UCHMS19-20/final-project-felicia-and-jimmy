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
class Puck(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLUE)
        self.image.set_colorkey(BLUE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity=[random.randint(4,8), random.randint(-8, 8)]
        self.rect=self.image.get_rect()

    def resetgame(self):
        self.x = random.randrange(50, 550)
        self.y=300.0
        self.speed=8.0
        self.direction=random.randrange(-45, 45)
        
    def bounce(self, diff):
        self.direction=(180-self.direction)%360
        self.direction-=diff
        self.velocity *= 1.1

    def update(self):
        if self.rect.y<0:
            self.resetgame()
        if self.rect.y>600:
            self.resetgame()
        if self.rect.x<=0:
            self.bounce()
        if self.rect.x>=600:
            self.bounce()

#create a paddle class from the Sprite class in pygame. Sprites are a base class for different types of obkects in a game.
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, 100, 10])

    def moveLeft(self, pixels):
        self.rect.x-=pixels
        if self.rect.x<0:
            self.rect.x=0

    def moveRight(self, pixels):
        self.rect.x+=pixels
        if self.rect.x>600:
            self.rect.x=600

paddleA=Paddle(WHITE, 100, 10)
paddleA.x=300
paddleA.y=20

paddleB=Paddle(WHITE, 100, 10)
paddleB.x=300
paddleB.y=580

puck=Puck(BLUE, 10, 10)
puck.rect.x=300
puck.rect.y=300

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(puck)


score1=0
score2=0

carryOn=True

#clearing screen and setting up midline
screen = pygame.display.set_mode( (600, 600) )
pygame.display.set_caption("Air Hockey")
screen.fill(BLACK)

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    pygame.draw.line(screen, (255, 255, 255), (0, 299), (600, 299),5)
    pygame.display.flip()

    #moving paddle when the user presses arrow keys (player A) or a/d keys (player B)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        paddleA.moveLeft(5)
    if keys[pygame.K_d]:
        paddleA.moveRight(5)
    if keys[pygame.K_LEFT]:
        paddleB.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddleB.moveRight(5)

    all_sprites_list.update()
   
    #check collision between paddle and puck
    if pygame.sprite.collide_mask(puck, paddleA) or pygame.sprite.collide_mask(puck, paddleB):
       puck.bounce()
