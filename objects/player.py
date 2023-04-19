import pygame


class Player:

    def __init__(self, player_name, player_health, player_damage, mana, player_level, placeholder, player_pos, player_weapon):
        self.img_path = "assets/textures/player.png"
        self.surface = pygame.image.load(self.img_path)
        self.name = player_name
        self.health = player_health
        self.damage = player_damage
        self.mana = mana
        self.level = player_level
        self.inventory = placeholder  # Awaiting to create the inventory class which will consist of a dictionary
        self.pos = player_pos
        self.weapon = player_weapon
