# IMPORTS --------------------------------------------------------------------------------------------------------------

import pygame
import time
import os  # Not used for now
import sys  # Not used for now
import cmd  # Not used for now
import random
import keyboard
import scripts.random_things as rt  # Not used for now
from objects.player import Player  # Not used for now

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
player = Player("firefood", 0, 0, 0, 0, 0, 0, 0)

# Other variables: controls, clock, delta time and air resistance
controls = {"up": "w",
            "left": "a",
            "down": "s",
            "right": "d"}
clock = pygame.time.Clock()
delta_time = clock.tick(60)
air_resistance = 0.99

running = True

# GAME LOOP ------------------------------------------------------------------------------------------------------------

while running:
    # Fills screen with black (the color wanted in "screen variables")
    screen.fill(screen_color)

    # Gets inputs from the keyboard and updates player's position
    player_direction = (keyboard.is_pressed(controls["right"]) - keyboard.is_pressed(controls["left"]),
                        keyboard.is_pressed(controls["up"]) - keyboard.is_pressed(controls["down"]))

    # Updates player's velocity variables
    player.velocity[0] += player_direction[0] * player.speed
    player.velocity[1] += player_direction[1] * player.speed
    player.velocity[0] *= air_resistance
    player.velocity[1] *= air_resistance

    # Updates variables of position
    player.pos[0] += player.velocity[0] * delta_time
    player.pos[1] -= player.velocity[1] * delta_time

    # Displays obstacles
    for wall in walls:
        wall[0].fill(wall_color)
        screen.blit(wall[0], (wall[1], wall[2]))
    screen.blit(player.surface, player.pos)

    # Updates the screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
