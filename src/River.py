import pygame


class River:

    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.length = self.screen.get_width()
        self.height = 210

    def draw(self):
        pygame.draw.rect(self.screen, (46, 107, 140), (self.x, self.y, self.length, 210))
