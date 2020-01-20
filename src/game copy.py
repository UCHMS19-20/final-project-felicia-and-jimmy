import sys
import pygame
import random

pygame.init()

screen = pygame.display.set_mode( (600, 600) )
pygame.display.set_caption("Air Hockey")
screen.fill(WHITE)
pygame.draw.line(screen, BLACK, (0, 299), (600, 299),5)
pygame.display.flip()