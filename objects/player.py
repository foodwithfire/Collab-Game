import pygame, keyboard
import [dossier].settings as settings


class Player:
    def __init__(self, screen, player_name, player_health, player_damage, mana, player_level, placeholder, player_weapon):
        self.screen = screen
        self.controls = settings.controls
        self.img_path = "assets/textures/player.png"
        self.surface = pygame.image.load(self.img_path)
        self.scale = 128

        self.name = player_name
        self.health = player_health
        self.damage = player_damage
        self.mana = mana
        self.level = player_level
        self.inventory = placeholder  # Awaiting to create the inventory class which will consist of a dictionary
        self.weapon = player_weapon

        self.pos = (0, 0)
        self.size = (50, 50)
        self.pos = [350, 250]
        self.speed = 1 / 1000
        self.velocity = [0, 0]
        self.air_resistance = 0.99

        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60)

    def update(self):
        player_direction = (keyboard.is_pressed(self.controls["right"]) - keyboard.is_pressed(self.controls["left"]),
                            keyboard.is_pressed(self.controls["up"]) - keyboard.is_pressed(self.controls["down"]))

        self.velocity[0] += player_direction[0] * self.speed
        self.velocity[1] += player_direction[1] * self.speed
        self.velocity[0] *= self.air_resistance
        self.velocity[1] *= self.air_resistance

        self.pos[0] += self.velocity[0] * self.delta_time
        self.pos[1] -= self.velocity[1] * self.delta_time

        self.surface = pygame.transform.scale(self.surface, (self.scale, self.scale))
        self.screen.blit(self.surface, self.pos)
