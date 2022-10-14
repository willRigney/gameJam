
# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((480, 720))
width = 750
height = 1500

# Add caption in the window
pygame.display.set_caption('Player Movement')

# Initializing the clock
# Clocks are used to track and
# control the frame-rate of a game
clock = pygame.time.Clock()

# creating a variable to check the direction
# of movementa
# We will change its value whenever
# the player changes its direction
direction = True


# Add player sprite
image = pygame.image.load("player.png")
image = pygame.transform.scale(image, (100, 100))
bg_img = pygame.image.load('background.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))



# Store the initial
# coordinates of the player in
# two variables i.e. x and y.
x = 100
y = 100

# Create a variable to store the
# velocity of player's movement
velocity = 12

player_speed = 4

i = 0
# Creating an Infinite loop
run = True
while run:

    # Set the frame rates to 60 fps
    clock.tick(60)

    # Filling the background with
    # white color
    window.fill((0,0,0))
    window.blit(bg_img,(i,0))

    # Display the player sprite at x
    # and y coordinates
    # Flipping the player sprite if player
    # changes the direction
    if direction == True:
        window.blit(image, (x, y))
    if direction == False:
        window.blit(pygame.transform.flip(image, True, False), (x, y))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # Closing the window and program if the
        # type of the event is QUIT
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        # Changing the value of the
        # direction variable
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                direction = False
            elif event.key == pygame.K_a:
                direction = True

    # Storing the key pressed in a
    # new variable using key.get_pressed()
    # method
    key_pressed_is = pygame.key.get_pressed()

    # Changing the coordinates
    # of the player
    if key_pressed_is[K_a]:
        x -= 10
        
    if key_pressed_is[K_d]:
        x += 10
        
    if key_pressed_is[K_w]:
        y -= 10
    if key_pressed_is[K_s]:
        y += 5
        

    y += player_speed
    # Draws the surface object to the screen.
    pygame.display.update()
