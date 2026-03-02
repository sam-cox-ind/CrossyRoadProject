"""
The  Controller  file for the Model-View-Controller architecture for our game.
Its   get_and_handle_events   method is called repeatedly by the main game loop.
At each call, it gets and handles whatever event(s) occurred,
typically by asking the various objects of the Game to do things.

Team members:
"""
# TODO: Put the names of your entire team in the above doc-string.

import pygame
import sys
from Game import Game


class Controller:
    def __init__(self, game: Game):
        self.game = game
        self.events = None  # For each cycle of the game loop, its events

    def get_and_handle_events(self):
        """
        Called by the main game loop.
        Gets events, then asks the Game's appropriate objects to handle them.
        """
        self.events = pygame.event.get()
        self.exit_if_time_to_quit()

        pressed_keys = pygame.key.get_pressed()

        # TODO: Use code like the following, but for YOUR Game objects.
        #     if pressed_keys[pygame.K_LEFT]:
        #         self.game.fighter.move_left()
        #     if pressed_keys[pygame.K_RIGHT]:
        #         self.game.fighter.move_right()
        #     if self.key_was_pressed_on_this_cycle(pygame.K_SPACE):
        #         self.game.fighter.fire()

        for event in self.events:
            if event.type == pygame.MOUSEBUTTONUP and self.game.menu.on_play_button():
                self.game.menu_open = False
            if event.type == pygame.MOUSEBUTTONUP and self.game.menu.on_green_player():
                if self.game.menu_open:
                    self.game.menu.player_color = "green"
                    self.game.game_over_menu.player_color = "green"
                    self.game.menu.player_selected_x = self.game.menu.green_player_x
            if event.type == pygame.MOUSEBUTTONUP and self.game.menu.on_red_player():
                if self.game.menu_open:
                    self.game.menu.player_color = "red"
                    self.game.game_over_menu.player_color = "red"
                    self.game.menu.player_selected_x = self.game.menu.red_player_x
            if event.type == pygame.MOUSEBUTTONUP and self.game.menu.on_blue_player():
                if self.game.menu_open:
                    self.game.menu.player_color = "blue"
                    self.game.game_over_menu.player_color = "blue"
                    self.game.menu.player_selected_x = self.game.menu.blue_player_x

            if event.type == pygame.MOUSEBUTTONUP and self.game.game_over_menu.on_play_button() and self.game.player.in_game is False:
                if self.game.player_is_dead:
                    self.game.game_reset = True
                if self.game.player_is_dead1:
                    self.game.game_reset = True

        if self.key_was_pressed_on_this_cycle(pygame.K_LEFT) and self.game.player.in_game:
            if not self.game.player_is_dead:
                if self.game.player.x > 13:
                    self.game.player.move_left()
        if self.key_was_pressed_on_this_cycle(pygame.K_RIGHT) and self.game.player.in_game:
            if not self.game.player_is_dead:
                if self.game.player.x < self.game.player.screen.get_width() - 13:
                    self.game.player.move_right()
        if self.key_was_pressed_on_this_cycle(pygame.K_UP) and self.game.player.in_game:
            if not self.game.player_is_dead:
                self.game.player.move_up()
                self.game.score.score += 10
                self.game.final_score.score += 10
        if self.game.player.y < self.game.screen.get_height() - 15:
            if not self.game.player_is_dead:
                if self.key_was_pressed_on_this_cycle(pygame.K_DOWN) and self.game.player.in_game:
                    self.game.player.move_down()
                    self.game.score.score -= 10
                    self.game.final_score.score -= 10

        # if self.game.player.pass_level():
            # self.game.player.y = self.game.player.screen.get_height() - 13

    def exit_if_time_to_quit(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                sys.exit()

    def key_was_pressed_on_this_cycle(self, key):
        """
        Returns True if the given key was pressed as one of the events
        that occurred on this cycle of the game loop.
        """
        for event in self.events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
