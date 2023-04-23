import pygame
import keyboard
import other.settings as settings

class Player:
    def __init__(self, args):
        self.screen = args[0]
        self.controls = settings.controls  # Gets the controls from the dictionary in settings
        self.img_path = "assets/textures/player.png"  # Put the player's texture in
        self.surface = pygame.image.load(self.img_path)  # Loads the image
        self.scale = args[9]  # Should remain 1 in buildings
        self.rect = pygame.rect.Rect((0, 0), (self.surface.get_size()[0]*self.scale, self.surface.get_size()[1]*self.scale))

        self.name = args[1]  # Should have the player specified name, "food" by default (or "firefood")
        self.health = args[2]  # 100 by default
        self.damage = args[3]  # 10 by default
        self.mana = args[4]  # 100 by default
        self.level = args[5]  # 0 by default
        self.inventory = args[6]
        self.weapon = args[7]  # Should be "fist" by default
        self.money = args[8] # Should be "100" by default

        self.player_direction = None
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
