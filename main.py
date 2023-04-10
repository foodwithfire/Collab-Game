import pygame, time, os, sys, cmd, random, keyboard

# screen vars
screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)

# player vars
player_size = (50, 50)
player_pos = [0, 0]
player_speed = 0.1

# setting vars
controls = {"up": "z",
            "left": "q",
            "down": "s",
            "right": "d"}
clock = pygame.time.Clock()
delta_time = clock.tick(60)

running = True
while running:
    # fill screen with black
    screen.fill((0, 0, 0))

    # get inputs and update the player position
    player_direction = (keyboard.is_pressed(controls["right"]) - keyboard.is_pressed(controls["left"]),
                        keyboard.is_pressed(controls["up"]) - keyboard.is_pressed(controls["down"]))
    player_pos[0] += player_direction[0] * player_speed * delta_time
    player_pos[1] -= player_direction[1] * player_speed * delta_time

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
