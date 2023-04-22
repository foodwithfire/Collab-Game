import pygame


class Button:
    def __init__(self, path1, path2, screen, scale):
        self.screen = screen
        self.surface_unpressed = pygame.image.load(path1)
        self.surface_pressed = pygame.image.load(path2)
        self.scale = scale
        self.size = self.surface_unpressed.get_size()
        self.surface_unpressed = pygame.transform.scale(self.surface_unpressed, (self.size[0]*self.scale, self.size[1]*self.scale))
        self.surface_pressed = pygame.transform.scale(self.surface_pressed, (self.size[0]*self.scale, self.size[1]*self.scale))
        self.mouse_pos = None

    def update(self, pos):
        self.mouse_pos = pygame.mouse.get_pos()
        self.pos = pos
        if (self.mouse_pos[0] > self.pos[0] and self.mouse_pos[0] < (self.pos[0] + self.size[0]*self.scale)) and\
           (self.mouse_pos[1] > self.pos[1] and self.mouse_pos[1] < (self.pos[1] + self.size[1]*self.scale)):
            if pygame.mouse.get_pressed()[0]:
                self.screen.blit(self.surface_pressed, self.pos)
            else:
                self.screen.blit(self.surface_unpressed, self.pos)
        else:
            self.screen.blit(self.surface_unpressed, self.pos)
