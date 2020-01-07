#create paddles for use in hockey
import pygame
BLACK=(0, 0, 0)

#create a paddle class from the Sprite class in pygame. Sprites are a base class for different types of obkects in a game.


    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()