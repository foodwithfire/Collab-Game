import pygame


class Button:
    def __init__(self, path1, path2, screen, scale, func):
        """
        Initiates:
            Screen
            Texture when pressed and when unpressed
            Scale
            Size
            Some rdm stuff
            Mouse position
            Function
        """
        self.screen = screen
        self.surface_unpressed = pygame.image.load(path1)
        self.surface_pressed = pygame.image.load(path2)
        self.scale = scale
        self.size = self.surface_unpressed.get_size()
        self.surface_unpressed = pygame.transform.scale(self.surface_unpressed, (self.size[0]*self.scale, self.size[1]*self.scale))
        self.surface_pressed = pygame.transform.scale(self.surface_pressed, (self.size[0]*self.scale, self.size[1]*self.scale))
        self.mouse_pos = None
        self.func = func

    def update(self, pos):  # Update function that updates the button
        self.mouse_pos = pygame.mouse.get_pos()
        self.pos = pos
        # If the mouse is on the button and if it gets pressed, then trigger the function
        if (self.mouse_pos[0] > self.pos[0] and self.mouse_pos[0] < (self.pos[0] + self.size[0]*self.scale)) and\
           (self.mouse_pos[1] > self.pos[1] and self.mouse_pos[1] < (self.pos[1] + self.size[1]*self.scale)):
            if pygame.mouse.get_pressed()[0]:
                self.screen.blit(self.surface_pressed, self.pos)
                self.func()
            else:
                self.screen.blit(self.surface_unpressed, self.pos)  # Else show the unpressed texture
        else:
            self.screen.blit(self.surface_unpressed, self.pos)  # Else show the unpressed texture
