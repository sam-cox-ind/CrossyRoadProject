import random

import pygame


class Log:
    def __init__(self, screen: pygame.Surface, x, y, level):
        self.screen = screen
        self.x = x
        self.y = y
        self.length = random.choice([60, 90])
        self.height = 30
        self.start = x
        self.level = level
        self.velocity = random.randint(1, 3) + level

    def draw(self):
        pygame.draw.rect(self.screen, (102, 53, 10), (self.x, self.y, self.length, self.height))
        pygame.draw.rect(self.screen, (112, 63, 10), (self.x + 20, self.y + 4, self.length - 40, 4))
        pygame.draw.rect(self.screen, (112, 63, 10), (self.x + 10, self.y + 13, self.length - 20, 4))
        pygame.draw.rect(self.screen, (112, 63, 10), (self.x + 20, self.y + 22, self.length - 40, 4))

    def move(self):
        if self.start == -30:
            self.x += self.velocity
        else:
            self.x -= self.velocity
