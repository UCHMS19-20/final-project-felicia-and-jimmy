import sys
import pygame
import random
pygame.init()

# Initialize pygame so it runs in the background and manages things

#defining colors

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
BLUE=(0, 255, 255)
screen = pygame.display.set_mode( (600, 600) )
pygame.display.set_caption("Air Hockey")
carryOn=True

clock = pygame.time.Clock()
while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn = False

    #clearing screen and setting up net
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [0, 299], [600, 299],5)

    #creating puck
    class Puck(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.surface([10, 10])
            self.image.fill(BLUE)
            self.rect=self.image.get_rect()
            self.screenheight=pygame.display.get_surface().get_height()
            self.screenwidth=pygame.display.get_surface().get_width()
            self.speed = 0
            self.x = 0
            self.y = 0
            self.direction = 0
            self.width = 10
            self.height = 10


   
    pygame.display.flip()

    clock.tick(60)

pygame.quit()