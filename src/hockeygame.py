import sys
import pygame
from paddle import Paddle

# Initialize pygame so it runs in the background and manages things
pygame.init()

#defining colors
LIGHTBLUE = (191, 239, 255)
WHITE=(255, 255, 255)

#setting up display
screen = pygame.display.set_mode( (700, 500) )
screen.fill(LIGHTBLUE)
pygame.display.set_caption("Air Hockey")

#create paddles
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x=20
paddleA.rect.y=200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x=665
paddleB.rect.y=200

screen.display.flip()


