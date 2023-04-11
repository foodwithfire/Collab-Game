import pygame, time, os, sys, cmd, random, keyboard

# screen vars
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

# player vars
player_size = (50, 50)
player_pos = [0, 0]
player_speed = 1/500
player_velocity_x = 0
player_velocity_y = 0

# setting vars
controls = {"up": "w",
            "left": "a",
            "down": "s",
            "right": "d"}
clock = pygame.time.Clock()
delta_time = clock.tick(60)
air_resistance = 0.98

running = True
while running:
    # fill screen with black
    screen.fill((0, 0, 0))

    # get inputs and update the player position
    player_direction = (keyboard.is_pressed(controls["right"]) - keyboard.is_pressed(controls["left"]),
                        keyboard.is_pressed(controls["up"]) - keyboard.is_pressed(controls["down"]))

    # update player's velocity
    player_velocity_x += player_direction[0] * player_speed
    player_velocity_y += player_direction[1] * player_speed
    player_velocity_x *= air_resistance
    player_velocity_y *= air_resistance

    # update player's position
    player_pos[0] += player_velocity_x * delta_time
    player_pos[1] -= player_velocity_y * delta_time

    # create the surface of the player and fill it with white
    player = pygame.Surface(player_size)
    player.fill((255, 255, 255))

    # display the player on the screen
    screen.blit(player, player_pos)

    # update the screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
