import pygame


class Image:
    def __init__(self, path, screen):
        self.img_path = path
        self.surface = pygame.image.load(self.img_path)
        self.screen = screen

    def update(self, pos):
        self.screen.blit(self.surface, pos)
