import random
import sys
import pygame
from pygame.locals import *
from text import *

# Initialize pygame so it runs and manages things
pygame.init()

# Create the screen and the clock
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Hockey")

#create clock so that the display screen updates every second (defined by FPS)
CLOCK = pygame.time.Clock()
FPS = 60

# defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


# creating puck
class Puck:
    def __init__(self):
        #get the image of the puck from the img folder and scale it to the screen
        self.image = pygame.image.load('src/img/bluecircle.png')  # Import the image
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize the image

        # Get a reference to the surface's rect and set the position to the centre of the screen
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        # Create the velocity and start direction variables
        self.velocity = pygame.math.Vector2()
        self.start_direction = 1

        #set conditions of playing and missed as false for later use in game logic
        self.playing = False
        self.missed = False

    def move(self):
        #update the position of the puck
        self.rect.move_ip(self.velocity) 

        # If the puck hits the left or right side of the screen, bounce off it
        if self.rect.left < 0:
            self.rect.left = 0
            self.bounce('x')

        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.bounce('x')

    def show(self):
        #display the puck on the screen
        screen.blit(self.image, self.rect)

    def reset(self):
        #reset the position and velocity of the puck
        self.velocity *= 0  # Set velocity to 0
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # Set position to centre of screen

        # reset conditions of puck for game logic
        self.playing = False
        self.missed = False

    def start(self):
        #start the game by moving the puck in a random direction
        self.velocity.y = 8 * self.start_direction  # Set the velocity to 8, and set the direction
        self.velocity.rotate_ip(random.uniform(-45, 45))  # Rotate the velocity vector by some random amount

        #update playing condition of puck
        self.playing = True  

    def bounce(self, axis):
        #bounce the puck in the given axis
        if axis == 'x':
            self.velocity.x *= -1
        elif axis == 'y':
            self.velocity.y *= -1
            # When bouncing off a puck, rotate velocity by a small random amount
            self.velocity.rotate_ip(random.uniform(-15, 15))
            #increase the velocity
            self.velocity *= 1.05  

    def check_hit(self, paddles):
        #check collisions with paddles
        for paddle in paddles:
            if paddle.rect.y < HEIGHT / 2:  # If it's the top paddle then
                if self.rect.top < paddle.rect.centery:  # If the puck has passed it
                    # If the puck is between the left and right edges of the paddle and hasn't missed it
                    if self.rect.right > paddle.rect.left and self.rect.left < paddle.rect.right and not self.missed:
                        self.bounce('y')  # Bounce in the y direction
                        self.rect.top = paddle.rect.centery  # Set the puck's y value to the y value of the paddle

                    else:
                        # If the puck has passed the paddle and isn't within the left and right edges, then flag missed
                        self.missed = True

            else:  # Same as above but for bottom paddle
                if self.rect.bottom > paddle.rect.centery:
                    if self.rect.right > paddle.rect.left and self.rect.left < paddle.rect.right and not self.missed:
                        self.bounce('y')
                        self.rect.bottom = paddle.rect.centery

                    else:
                        self.missed = True

    def check_miss(self, scores, score_text):
        #check if the puck has missed the paddle and give points accordingly
        if self.rect.top > HEIGHT:  # If the puck has gone off the bottom of the screen
            self.reset()  # Reset puck
            self.start_direction = -1  # Set start direction to other player

            scores[0] += 1  # Increment score
            score_text[0].set_text(scores[0])  # Update text

        elif self.rect.bottom < 0:  # Same as above for other player
            self.reset()
            self.start_direction = 1

            scores[1] += 1
            score_text[1].set_text(scores[1])


class Paddle:
    def __init__(self, x, y):
        #defining paddles controlled by players--load the image from the img folder and resize
        self.image = pygame.image.load('src/img/blackrectangle.png') 
        self.image = pygame.transform.scale(self.image, (200, 100)) 
        # Get a reference to the surface's rect and set the position to the centre of the screen
        self.rect = self.image.get_rect(center=(x, y))

    def show(self):
        #display paddle on screen
        screen.blit(self.image, self.rect)

    def moveLeft(self, pixels):
        #move the paddle left and stop the paddle when it reaches the left wall
        self.rect.x -=pixels
        if self.rect.x<0:
            self.rect.x=0
    def moveRight(self, pixels):
        #move the paddle right and stop the paddle when it reaches the right wall
        self.rect.x +=pixels
        if self.rect.x>600:
            self.rect.x=600

    def move_left(self, pixels):
        #move left function for the other paddle
        self.rect.x -= pixels 
        if self.rect.x < 0: 
            self.rect.x = 0

    def move_right(self, pixels):
        #move right function for other paddle
        self.rect.x += pixels 
        if self.rect.right > WIDTH:  
            self.rect.right = WIDTH

def menu():
    # Set all the text to show on the menu screen
    menu_text = Text((WIDTH / 2, 100), "Air Hockey", BLACK, 64, anchor="center")

    instruction_text = [Text((WIDTH / 2, 270), "Instructions:", BLACK, 24, anchor="center"),
                        Text((WIDTH / 2, 300), "Press SPACE to start the game, then use the", BLACK, 16, anchor="center"),
                        Text((WIDTH / 2, 320), "ARROW KEYS or A and D to move your paddle.", BLACK, 16, anchor="center"),
                        Text((WIDTH / 2, 350), "Use your paddle to knock the puck back at", BLACK, 16, anchor="center"),
                        Text((WIDTH / 2, 370), "you opponent, but don't miss it when it comes", BLACK, 16, anchor="center"),
                        Text((WIDTH / 2, 390), "towards you! You will gain a point by getting", BLACK, 16, anchor="center"),
                        Text((WIDTH / 2, 410), "it past your opponent.", BLACK, 16, anchor="center"),
                        Text((WIDTH / 2, 500), "SPACE TO START", BLACK, 32, anchor="center")]
    #set started condition for use in game logic
    started = False  
    
    
    
    # Main loop
    while not started:
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, (100, 250, 400, 175))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #start game when space key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    started = True  

        # Render all text to the screen
        menu_text.render(screen)
        for line in instruction_text:
            line.render(screen)

        pygame.display.update()  # Update the screen

    game()  # Start the game


def draw_table():
    #draw background on the screen
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(WIDTH / 2), int(HEIGHT / 2)), 50, 5)
    pygame.draw.circle(screen, BLUE, (int(WIDTH / 2), 0), 100, 5)
    pygame.draw.circle(screen, BLUE, (int(WIDTH / 2), HEIGHT), 100, 5)
    pygame.draw.line(screen, BLACK, (0, HEIGHT / 2), (WIDTH, HEIGHT / 2), 5)


def game():
   
    # Create game objects
    puck = Puck()
    paddles = [Paddle(300, 550), Paddle(300, 50)]

    # Setup scores
    scores = [0, 0]
    score_text = [Text((10, 250), scores[0], BLACK),
                  Text((10, 295), scores[1], BLACK)]

    # Main loop
    while True:
        #update screen with clock, draw background
        clock=pygame.time.Clock()
        draw_table()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            #start puck movement when space key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    if not puck.playing:
                        puck.start()
 

        # Update the puck-check if it collides
        puck.move()
        puck.check_hit(paddles)
        puck.check_miss(scores, score_text)

        keys = pygame.key.get_pressed()
        # moving paddle when the user presses arrow keys (player A) or a/d keys (player B)
        if keys[pygame.K_a]:
            paddles[0].move_left(10)
        if keys[pygame.K_d]:
            paddles[0].move_right(10)
        if keys[pygame.K_LEFT]:
            paddles[1].move_left(10)
        if keys[pygame.K_RIGHT]:
            paddles[1].move_right(10)


        # Display all game objects and score
        puck.show()
        for paddle in paddles:
            paddle.show()
        for text in score_text:
            text.render(screen)

        pygame.display.update()  # Update the screen
        CLOCK.tick(FPS)  # Limit game to frames per second


    pygame.display.update()
    pygame.display.flip()


if __name__ == '__main__':
    menu()             