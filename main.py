# IMPORTS --------------------------------------------------------------------------------------------------------------

import pygame
import time
import os  # Not used for now
import sys  # Not used for now
import cmd  # Not used for now
import random
import keyboard
import scripts.random_things as rt  # Not used for now
from objects.player import Player
from objects.button import Button

# VARIABLES SETTING-UP -------------------------------------------------------------------------------------------------

# Screen variables: size, color; sets "screen" as a screen display
screen_size = (800, 600)
screen_color = (0, 0, 0)
screen = pygame.display.set_mode(screen_size)

# Obstacles variables; not used for now: size, density, color, and an empty array
wall_size = (20, 20)
wall_density = 0
wall_color = (150, 150, 150)
walls = []
if wall_density != 0:
    for y in range(int(screen_size[1] / wall_size[0])):
        for x in range(int(screen_size[0] / wall_size[0])):
            if random.randint(0, 100) < wall_density:
                walls.append((pygame.Surface(wall_size), x * wall_size[0], y * wall_size[0]))

# Player
player = Player(screen, "firefood", 0, 0, 0, 0, 0, 0)
# Button
button1 = Button((150, 100), (200, 100), screen)

# GAME LOOP ------------------------------------------------------------------------------------------------------------
running = True
while running:
    # Fills screen with black (the color wanted in "screen variables")
    screen.fill(screen_color)

    # Displays obstacles
    for wall in walls:
        wall[0].fill(wall_color)
        screen.blit(wall[0], (wall[1], wall[2]))

    # Updates the screen
    player.update()
    button1.update()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
