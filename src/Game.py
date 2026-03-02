"""
The  Game (model)  file for the Model-View-Controller architecture for our game.
1. It constructs all the objects specific to this game.
2. Its   draw_game   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to draw themselves.
3. Its   run_one_cycle   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to do whatever needs to happen
   independently of events / user-input.

Team members:
Huan Zhang, Sam Cox
"""
# TODO: Put the names of your entire team in the above doc-string.
import random

import pygame
from Logs import Logs
from Cars import Cars
from Player import Player
from ScoreBoard import ScoreBoard


# TODO: Put each class in its own module, using the same name for both.
#  Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter
#     from Missiles import Missiles
#     from Enemies import Enemies


class Game:
    def __init__(self, screen: pygame.Surface, level, menu, game_over_menu):
        self.screen = screen
        self.y = 60
        self.y2 = 360
        self.level = level
        self.menu = menu
        self.menu_open = True
        self.on_log = False
        self.player_is_dead1 = False
        self.player_is_dead = False
        self.game_over_menu = game_over_menu
        self.game_reset = False
        self.hit_by_car = pygame.mixer.Sound("CARCR111.wav")
        self.drown = pygame.mixer.Sound("drown1.wav")

        # TODO: Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)
        #     self.enemies = Enemies(self.screen)
        # self.car = Car(self.screen, random.choice(self.spawn_car), random.randint(300, 600))

        self.cars = Cars(self.screen, 0, self.y, self.level)
        self.cars2 = Cars(self.screen, 0, self.y2, self.level)
        self.logs = Logs(self.screen, 0, self.y, self.level)
        self.logs2 = Logs(self.screen, 0, self.y2, self.level)
        self.obstacles1 = random.choice([self.cars, self.logs])
        self.obstacles2 = random.choice([self.cars2, self.logs2])
        self.score = ScoreBoard(self.screen, self.level, 5, 30)
        self.final_score = ScoreBoard(self.screen, self.level, screen.get_height() - 280, 40)
        self.player = Player(screen, screen.get_width() // 2, screen.get_height() - 15, self.menu)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # TODO: Use something like the following, but for objects in YOUR game:
        #     self.fighter.draw()
        #     self.missiles.draw()
        #     self.enemies.draw()
        self.obstacles1.draw()
        self.obstacles2.draw()
        self.player.draw()
        self.score.draw()
        if self.level == 1 and self.menu_open:
            self.menu.draw()
        else:
            self.player.in_game = True

        if self.player_is_dead:
            self.game_over_menu.draw()
            self.final_score.draw()
            self.player.in_game = False
        if self.player_is_dead1:
            self.game_over_menu.draw()
            self.final_score.draw()
            self.player.in_game = False

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # TODO: Use something like the following, but for objects in YOUR game:
        #     self.missiles.move()
        #     self.enemies.move()
        #     self.missiles.handle_explosions(self.enemies)

        self.obstacles1.spawn()
        self.obstacles2.spawn()
        self.obstacles1.delete()
        self.obstacles2.delete()
        self.obstacles1.close_to1()
        self.obstacles1.close_to2()
        self.obstacles2.close_to1()
        self.obstacles2.close_to2()

        if not self.player_is_dead:
            if self.obstacles1 == self.cars:
                for car in self.obstacles1.new_cars:
                    car.move()
                for car in self.obstacles1.new_cars2:
                    car.move()
            if self.obstacles1 == self.logs:
                for log in self.obstacles1.new_logs:
                    log.move()
                for log in self.obstacles1.new_logs2:
                    log.move()
            if self.obstacles2 == self.cars2:
                for car in self.obstacles2.new_cars:
                    car.move()
                for car in self.obstacles2.new_cars2:
                    car.move()
            if self.obstacles2 == self.logs2:
                for log in self.obstacles2.new_logs:
                    log.move()
                for log in self.obstacles2.new_logs2:
                    log.move()

            if self.player.x > self.screen.get_width():
                self.player_is_dead = True
                self.drown.play()

            if self.player.x < 0:
                self.player_is_dead = True
                self.drown.play()

        if self.obstacles1 == self.cars:
            for car in self.obstacles1.new_cars:
                if self.player.hit_by(car):
                    self.player_is_dead = True
                    self.player_is_dead1 = True
                    self.hit_by_car.play()

            for car in self.obstacles1.new_cars2:
                if self.player.hit_by(car):
                    self.player_is_dead = True
                    self.player_is_dead1 = True
                    self.hit_by_car.play()

        if self.obstacles2 == self.cars2:
            for car in self.obstacles2.new_cars:
                if self.player.hit_by(car):
                    self.player_is_dead = True
                    self.player_is_dead1 = True
                    self.hit_by_car.play()

            for car in self.obstacles2.new_cars2:
                if self.player.hit_by(car):
                    self.player_is_dead = True
                    self.player_is_dead1 = True
                    self.hit_by_car.play()

        if self.obstacles1 == self.logs:
            if self.player.hit_by(self.obstacles1.river):
                self.on_log = False
                for log in self.obstacles1.new_logs:
                    if self.player.hit_by(log):
                        self.player.x -= log.velocity
                        self.player.left_eye = (self.player.x - 8, self.player.y - 7)
                        self.player.right_eye = (self.player.x + 8, self.player.y - 7)
                        self.on_log = True

                for log in self.obstacles1.new_logs2:
                    if self.player.hit_by(log):
                        self.player.x += log.velocity
                        self.player.left_eye = (self.player.x - 8, self.player.y - 7)
                        self.player.right_eye = (self.player.x + 8, self.player.y - 7)
                        self.on_log = True

                if not self.on_log:
                    self.player_is_dead = True
                    self.drown.play()

        if self.obstacles2 == self.logs2:
            if self.player.hit_by(self.obstacles2.river):
                self.on_log = False
                for log in self.obstacles2.new_logs:
                    if self.player.hit_by(log):
                        self.player.x -= log.velocity
                        self.player.left_eye = (self.player.x - 8, self.player.y - 7)
                        self.player.right_eye = (self.player.x + 8, self.player.y - 7)
                        self.on_log = True

                for log in self.obstacles2.new_logs2:
                    if self.player.hit_by(log):
                        self.player.x += log.velocity
                        self.player.left_eye = (self.player.x - 8, self.player.y - 7)
                        self.player.right_eye = (self.player.x + 8, self.player.y - 7)
                        self.on_log = True

                if not self.on_log:
                    self.player_is_dead = True
                    self.drown.play()
