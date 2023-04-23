# IMPORTS --------------------------------------------------------------------------------------------------------------
import scripts.random_things as rt
from classes.image import *
from objects.button import *
from objects.player import Player

import classes.inventory as inv

# Initiating Pygame
pygame.init()

# VARIABLES SETTING-UP -------------------------------------------------------------------------------------------------

# Screen variables: size, color; sets "screen" as a screen display
screen_size = (800, 600)
screen_color = (0, 0, 0)
screen = pygame.display.set_mode(screen_size)

# Inventory setting-up
inventory = [inv.inventory_slots, inv.hotbar]

# Setting the menu
main_menu = Image("assets/textures/gui/main_menu/main_menu.png", screen)
started = False
player = None

# Start function for the menu, comes from Random Things
background = Image("assets/textures/map/buildings/food_house.png", screen)


def start():
    """
    Starts the game. Takes as args, in the order:
    screen, player_name, player_health, player_damage, mana, player_level, inventory, player_weapon, player_money
    """
    global player, started, background
    player = Player((screen, "food", 0, 0, 0, 0, 0, 0, 0, 1))
    started = True


# Play button
main_menu_play_button = Button("assets/textures/buttons/main_menu/play_unpressed.png", "assets/textures/buttons/main_menu/play_pressed.png", screen, 4, start)

# GAME LOOP ------------------------------------------------------------------------------------------------------------
running = True
while running:
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
