# IMPORTS --------------------------------------------------------------------------------------------------------------

import pygame
import time
import os  # Not used for now
import sys  # Not used for now
import cmd  # Not used for now
import random
import keyboard
import scripts.random_things as rt  # Not used for now
from objects.image import *
from objects.player import *
from objects.button import *

# VARIABLES SETTING-UP -------------------------------------------------------------------------------------------------

# Screen variables: size, color; sets "screen" as a screen display
screen_size = (800, 600)
screen_color = (0, 0, 0)
screen = pygame.display.set_mode(screen_size)

main_menu = Image("assets/textures/gui/main_menu/main_menu.png", screen)
started = False
player = None


def start():
    global player, started, background
    player = Player(screen, "food", 0, 0, 0, 0, 0, 0)
    background = Image("assets/textures/map/buildings/food_house.png", screen)
    started = True


main_menu_play_button = Button("assets/textures/buttons/main_menu/play_unpressed.png", "assets/textures/buttons/main_menu/play_pressed.png", screen, 4, start)

# GAME LOOP ------------------------------------------------------------------------------------------------------------
running = True
while running:
    screen.fill("white")
    if started:
        background.update((0, 0))
        player.update()
    else:
        main_menu.update((0, 0))
        main_menu_play_button.update((350, 250))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
