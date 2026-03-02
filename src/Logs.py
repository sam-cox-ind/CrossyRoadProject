import random

import pygame

from Log import Log
from River import River


class Logs:
    def __init__(self, screen: pygame.Surface, x, y, level):
        self.screen = screen
        self.x = x
        self.y = y
        self.new_logs = []
        self.new_logs2 = []
        self.river = River(self.screen, self.x, self.y)
        self.level = level

    def draw(self):
        self.river.draw()
        for log in self.new_logs:
            log.draw()

        for log in self.new_logs2:
            log.draw()

    def spawn(self):
        new_log = Log(self.screen, self.screen.get_width(),
                      self.y + random.choice([0, 60, 120, 180]), self.level)
        new_log2 = Log(self.screen, -30,
                       self.y + random.choice([30, 90, 150]), self.level)

        if len(self.new_logs) < 40:
            if len(self.new_logs) == 0:
                self.new_logs.append(new_log)
            if len(self.new_logs) > 0:
                if self.new_logs[len(self.new_logs) - 1].x < self.screen.get_width() - 100:
                    self.new_logs.append(new_log)

        if len(self.new_logs2) < 30:
            if len(self.new_logs2) == 0:
                self.new_logs2.append(new_log2)
            if len(self.new_logs2) > 0:
                if self.new_logs2[len(self.new_logs2) - 1].x > 100:
                    self.new_logs2.append(new_log2)

    def delete(self):
        for k in range(len(self.new_logs) - 1, -1, -1):
            if self.new_logs[k].x < -60:
                del self.new_logs[k]

        for k in range(len(self.new_logs2) - 1, -1, -1):
            if self.new_logs2[k].x > self.screen.get_width() + 5:
                del self.new_logs2[k]

    def close_to1(self):
        for k in range(len(self.new_logs) - 1, -1, -1):
            log = self.new_logs[k]
            for log2 in self.new_logs:
                hit_box1 = pygame.Rect(log.x + 20, log.y, log.length + 40, log.height)
                hit_box2 = pygame.Rect(log2.x + 20, log2.y, log2.length + 40, log2.height)
                if hit_box1.colliderect(hit_box2):
                    log.velocity = log2.velocity

    def close_to2(self):
        for k in range(len(self.new_logs2) - 1, -1, -1):
            log = self.new_logs2[k]
            for log2 in self.new_logs2:
                hit_box1 = pygame.Rect(log.x - 20, log.y, log.length + 40, log.height)
                hit_box2 = pygame.Rect(log2.x - 20, log2.y, log2.length + 40, log2.height)
                if hit_box1.colliderect(hit_box2):
                    log.velocity = log2.velocity
