import pygame

class Button:
    def __init__(self, pos, size, screen, text=None):
        self.pos = pos
        self.size = size
        self.screen = screen
        self.text = text
        self.surface = pygame.Surface(self.size)

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if (self.mouse_pos[0] > self.pos[0] and self.mouse_pos[0] < (self.pos[1] + self.size[0])) and\
           (self.mouse_pos[1] > self.pos[1] and self.mouse_pos[1] < (self.pos[1] + self.size[1])):
            if pygame.mouse.get_pressed()[0]:
                self.color = (255, 255, 255)
            else:
                self.color = (170, 170, 170)
        else:
            self.color = (70, 70, 70)
        self.surface.fill(self.color)
        self.screen.blit(self.surface, self.pos)