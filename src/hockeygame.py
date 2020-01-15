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
    def __init__(self):
        super().__init__()
        self.image = pygame.surface([10, 10])
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.speed = 0
        self.x = 0
        self.y = 0
        self.direction = 0
        self.width = 10
        self.height = 10
        self.resetgame()

    def resetgame(self):
        self.x = random.randrange(50, 550)
        self.y=300.0
        self.speed=8.0
        self.direction=random.randrange(-45, 45)
        
    def bounce(self, diff):
        self.direction=(180-self.direction)%360
        self.direction-=diff
        self.speed *= 1.1

    def update(self):
        if self.y<0:
            self.resetgame()
        if self.y>600:
            self.resetgame()
        if self.x<=0:
            self.bounce()
        if self.x>=600:
            self.bounce()

class Player(pygame.sprite.Sprite):
    def __init__(self, joystick, ypos):
        super().__init__()
        self.width=75
        self.height=15
        self.image=pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.joystick=joystick

        self.rect=self.image.get_rect()
        self.screenheight=pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x=0
        self.rect.y=ypos

    def update(self):
        xaxis_pos=self.joystick.get_axis(0)
        self.rect.x=self.rect.x+xaxis_pos*15
        if self.rect.x>600:
            self.rect.x=600
        if self.rect.x<0:
            self.rect.x=0
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

   