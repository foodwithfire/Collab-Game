import pygame, keyboard
import Foods_Legend.settings as settings


class Player:
    def __init__(self, screen, player_name, player_health, player_damage, mana, player_level, placeholder, player_weapon):
        self.screen = screen
        self.controls = settings.controls
        self.img_path = "assets/textures/player.png"
        self.surface = pygame.image.load(self.img_path)
        self.rect = pygame.rect.Rect((0, 0), self.surface.get_size())
        self.scale = 48

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
        self.speed = 0.1

        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60)

    def update(self):
        self.rect = pygame.rect.Rect(self.pos, self.surface.get_size())
        self.player_direction = (
            keyboard.is_pressed(self.controls["right"]) - keyboard.is_pressed(self.controls["left"]),
            keyboard.is_pressed(self.controls["up"]) - keyboard.is_pressed(self.controls["down"])
)
        self.pos[0] += self.player_direction[0] * self.speed * self.delta_time
        self.pos[1] -= self.player_direction[1] * self.speed * self.delta_time

        self.surface = pygame.transform.scale(self.surface, (self.scale, self.scale))
        self.screen.blit(self.surface, self.pos)
