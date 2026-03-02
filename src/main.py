"""
The  main  file for the Model-View-Controller (MVC) architecture for our game.
It:
   1. Initializes pygame, the screen and a Clock (for the frame rate).
   2. Constructs a Game (model), View and Controller.
   3. Runs the game loop, which repeatedly (per the frame rate):
      -- Asks the Controller object to get and respond to events.
      -- Asks the Game object to run one cycle.
      -- Asks the View object to draw everything.

Team members:
"""
# TODO: Put the names of your entire team in the above doc-string.

import pygame
from Game import Game
from Controller import Controller
from View import View
from Menu import Menu


# def run_game_loop(clock, frame_rate, controller, game, view, screen, level):
#     while True:
#         clock.tick(frame_rate)
#         controller.get_and_handle_events()
#         game.run_one_cycle()
#         view.draw_everything()
#         # game.player.speed += 0.5 * (level - 1)
#
#         if game.player.pass_level():
#             level += 1
#             screen = pygame.display.set_mode((640, 660))  # TODO: Choose your own size
#             clock = pygame.time.Clock()
#             game = Game(screen, level)
#             view = View(screen, game)
#             controller = Controller(game)
#             run_game_loop(clock, frame_rate, controller, game, view, screen, level)


def main():
    pygame.init()
    pygame.display.set_caption("2D Crossy Road")  # TODO: Put your own game name
    screen = pygame.display.set_mode((640, 660))  # TODO: Choose your own size
    clock = pygame.time.Clock()
    level = 1
    menu = Menu(screen, "2D Crossy Road", "Play", True)
    game_over_menu = Menu(screen, "Game Over", "Play Again", False)
    game = Game(screen, level, menu, game_over_menu)  # the Model
    view = View(screen, game)  # the View
    controller = Controller(game)  # the Controller
    frame_rate = 60  # TODO: Choose your own frame rate

    # This runs a game loop that has recursion but also allows a main menu
    # run_game_loop(clock, frame_rate, controller, game, view, screen, level)

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
        view.draw_everything()

        if game.player.pass_level():
            level += 1
            screen = pygame.display.set_mode((640, 660))
            clock = pygame.time.Clock()
            game = Game(screen, level, menu, game_over_menu)
            view = View(screen, game)
            controller = Controller(game)

        if game.game_reset:
            level = 1
            screen = pygame.display.set_mode((640, 660))
            clock = pygame.time.Clock()
            game = Game(screen, level, menu, game_over_menu)
            view = View(screen, game)
            controller = Controller(game)

        pygame.display.update()


main()
