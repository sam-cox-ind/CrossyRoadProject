import random

import pygame

from Car import Car


class Cars:
    def __init__(self, screen: pygame.Surface, x, y, level):
        self.screen = screen
        self.x = x
        self.y = y
        self.new_cars = []
        self.new_cars2 = []
        self.level = level

    def draw(self):
        pygame.draw.rect(self.screen, "dark grey", (self.x, self.y, self.screen.get_width(), 210))
        for k in range(8):
            pygame.draw.line(self.screen, "white", (self.x, self.y + 30 * k),
                             (self.screen.get_width(), self.y + 30 * k), 2)
        for car in self.new_cars:
            car.draw()

        for car in self.new_cars2:
            car.draw()

    def spawn(self):
        new_car = Car(self.screen, self.screen.get_width(),
                      self.y + random.choice([0, 60, 120, 180]), self.level)
        new_car2 = Car(self.screen, -30,
                       self.y + random.choice([30, 90, 150]), self.level)

        if len(self.new_cars) < 12:
            if len(self.new_cars) == 0:
                self.new_cars.append(new_car)
            if len(self.new_cars) > 0:
                if self.new_cars[len(self.new_cars) - 1].x < self.screen.get_width() - 90:
                    self.new_cars.append(new_car)

        if len(self.new_cars2) < 9:
            if len(self.new_cars2) == 0:
                self.new_cars2.append(new_car2)
            if len(self.new_cars2) > 0:
                if self.new_cars2[len(self.new_cars2) - 1].x > 90:
                    self.new_cars2.append(new_car2)

    def delete(self):
        for k in range(len(self.new_cars) - 1, -1, -1):
            if self.new_cars[k].x < -60:
                del self.new_cars[k]

        for k in range(len(self.new_cars2) - 1, -1, -1):
            if self.new_cars2[k].x > self.screen.get_width() + 5:
                del self.new_cars2[k]

    def close_to1(self):
        for k in range(len(self.new_cars) - 1, -1, -1):
            car = self.new_cars[k]
            for car2 in self.new_cars:
                hit_box1 = pygame.Rect(car.x, car.y, car.length + 15, car.height)
                hit_box2 = pygame.Rect(car2.x, car2.y, car2.length + 15, car2.height)
                if hit_box1.colliderect(hit_box2):
                    car.velocity = car2.velocity

    def close_to2(self):
        for k in range(len(self.new_cars2) - 1, -1, -1):
            car = self.new_cars2[k]
            for car2 in self.new_cars2:
                hit_box1 = pygame.Rect(car.x, car.y, car.length + 15, car.height)
                hit_box2 = pygame.Rect(car2.x, car2.y, car2.length + 15, car2.height)
                if hit_box1.colliderect(hit_box2):
                    car.velocity = car2.velocity
