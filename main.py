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

# Player variables: size, color, position, speed, velocity
player_size = (50, 50)
player_color = (255, 255, 255)
player_pos = [350, 250]
player_speed = 1/1000
player_velocity = [0, 0]

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
    player_velocity[0] += player_direction[0] * player_speed
    player_velocity[1] += player_direction[1] * player_speed
    player_velocity[0] *= air_resistance
    player_velocity[1] *= air_resistance

    # Updates variables of position
    player_pos[0] += player_velocity[0] * delta_time
    player_pos[1] -= player_velocity[1] * delta_time

    # Creates the "player": a white square of the color and size chosen in player variables
    player = Player("firefood", 0, 0, 0, 0, 0, 0, 0)

    # Displays obstacles
    for wall in walls:
        wall[0].fill(wall_color)
        screen.blit(wall[0], (wall[1], wall[2]))
    screen.blit(player.surface, player_pos)

    # Updates the screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
