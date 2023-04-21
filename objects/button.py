import pygame


class Button:
    def __init__(self, path, pos, screen):
        self.path = path
        self.pos = pos
        self.screen = screen
        self.surface = pygame.image.load(self.path)
        self.size = self.surface.get_size()
        self.mouse_pos = None

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if (self.mouse_pos[0] > self.pos[0] and self.mouse_pos[0] < (self.pos[1] + self.size[0])) and\
           (self.mouse_pos[1] > self.pos[1] and self.mouse_pos[1] < (self.pos[1] + self.size[1])):
            if pygame.mouse.get_pressed()[0]:
                print("pressed")
        self.screen.blit(self.surface, self.pos)
