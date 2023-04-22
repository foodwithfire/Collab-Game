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

# Player
player = Player(screen, "firefood", 0, 0, 0, 0, 0, 0)
# Button
button1 = Button("assets/textures/player.png", (0, 0), screen)
# Background
main_menu = Image("assets/textures/gui/main_menu/main_menu.png", screen)

# GAME LOOP ------------------------------------------------------------------------------------------------------------
running = True
while running:

    main_menu.update((0, 0))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
