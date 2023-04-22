import pygame
import keyboard
import other.settings as settings


class Player:
    def __init__(self, screen, player_name, player_health, player_damage, mana, player_level, placeholder, player_weapon, scale):
        self.screen = screen
        self.controls = settings.controls  # Gets the controls from the dictionary in settings
        self.img_path = "assets/textures/player.png"  # Put the player's texture in
        self.surface = pygame.image.load(self.img_path)  # Loads the image
        self.scale = scale  # Should remain 48 in buildings
        self.rect = pygame.rect.Rect((0, 0), (self.surface.get_size()[0]*self.scale, self.surface.get_size()[1]*self.scale))

        self.name = player_name  # Should have the player specified name, "food" by default (or "firefood")
        self.health = player_health  # 100 by default
        self.damage = player_damage  # 10 by default
        self.mana = mana  # 100 by default
        self.level = player_level  # 0 by default
        self.inventory = placeholder  # Awaiting to create the inventory class which will consist of a dictionary
        self.weapon = player_weapon  # Should be "knife" by default

        self.pos = (0, 0)
        self.pos = [350, 250]
        self.speed = 0.1

        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60)

    def update(self):
        self.rect = pygame.rect.Rect(self.pos, (self.surface.get_size()[0]*self.scale, self.surface.get_size()[1]*self.scale))
        # Defines the direction
        self.player_direction = (
            keyboard.is_pressed(self.controls["right"]) - keyboard.is_pressed(self.controls["left"]),
            keyboard.is_pressed(self.controls["up"]) - keyboard.is_pressed(self.controls["down"])
)
        # Hard math for the player motion
        self.pos[0] += self.player_direction[0] * self.speed * self.delta_time
        self.pos[1] -= self.player_direction[1] * self.speed * self.delta_time

        # Scaling the player
        self.surface = pygame.transform.scale(self.surface, (self.surface.get_size()[0]*self.scale, self.surface.get_size()[1]*self.scale))
        self.screen.blit(self.surface, self.pos)
