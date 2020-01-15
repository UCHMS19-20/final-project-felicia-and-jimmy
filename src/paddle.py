#create paddles for use in hockey
import pygame
WHITE=(255, 255, 255)

#create a paddle class from the Sprite class in pygame. Sprites are a base class for different types of obkects in a game.
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image=pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect=self.image.get.rect()

        def moveLeft(self, pixels):
            self.rect.x-=pixels
            if self.rect.x<0:
                self.rect.x=0

        def moveRight(self, pixels):
            self.rect.x+=pixels
            if self.rect.x>600:
                self.rect.x=600
            