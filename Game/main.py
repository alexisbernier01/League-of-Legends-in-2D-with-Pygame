import pygame
import sys

from entities import Player, Minion, Turret, Nexus

pygame.init()
width, height = 1280, 720

screen = pygame.display.set_mode((width, height)) # Initializes pygame display 'Surface' to for display.
font = pygame.font.SysFont('Candara', 30) 
clock = pygame.time.Clock() 

player = Player()
minion = Minion()
turret = Turret()
nexus = Nexus()

print(minion.hitpoints)

# Game loop
while True:
    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    screen.fill("black")
    screen.blit(player.img, player.img_rect)
    pygame.display.update()
    clock.tick(200)



    


