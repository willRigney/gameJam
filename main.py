from turtle import Screen
import pygame, sys

# general setup
pygame.init()
clock = pygame.time.Clock()

# setting up the main window
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Spooky Scary Space Ghost")
color = (255,0, 0)
screen.fill(color)

#sprites
player = pygame.Rect(screen_width/2 - 25 ,screen_height/2 - 25, 50, 50)
ghost = pygame.Rect(100, 100 ,50 ,50)

white = (0, 0 ,0)

pygame.draw.rect(screen, white, player)
pygame.draw.rect(screen, white, ghost)

player_speed = -5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.W_DOWN:
                player_speed += 10
        
    pygame.display.flip()
    clock.tick(60)