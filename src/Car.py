import random

import pygame


class Car:
    def __init__(self, screen: pygame.Surface, x, y, level):
        self.screen = screen
        self.x = x
        self.y = y
        self.height = 30
        self.length = random.choice([60, 90])
        self.r = random.randint(100, 250)
        self.g = random.randint(100, 250)
        self.b = random.randint(100, 250)
        self.start = x
        self.level = level
        self.velocity = random.randint(1, 4) + level

    def draw(self):
        pygame.draw.rect(self.screen, (self.r, self.g, self.b), (self.x, self.y, self.length, self.height))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x + self.length / 2 - 12, self.y + 3, 24, 24))
        pygame.draw.line(self.screen, (0, 0, 0), (self.x + 3, self.y), (self.x + self.length / 2 - 20, self.y))
        pygame.draw.line(self.screen, (0, 0, 0), (self.x + 3, self.y + 30),
                         (self.x + self.length / 2 - 20, self.y + 30))
        pygame.draw.line(self.screen, (0, 0, 0), (self.x + self.length / 2 + 20, self.y),
                         (self.x + self.length - 3, self.y))
        pygame.draw.line(self.screen, (0, 0, 0), (self.x + self.length / 2 + 20, self.y + 30),
                         (self.x + self.length - 3, self.y + 30))

    def move(self):
        if self.start == -30:
            self.x += self.velocity
        else:
            self.x -= self.velocity


