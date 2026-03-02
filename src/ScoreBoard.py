import pygame


class ScoreBoard:
    def __init__(self, screen, level, y, size):
        self.screen = screen
        self.score = (level - 1) * 220
        self.font = pygame.font.Font(None, size)
        self.y = y

    def draw(self):
        score_string = ("Score: {}".format(self.score))
        score_image = self.font.render(score_string, True, (255, 255, 255))
        self.screen.blit(score_image, ((self.screen.get_width() // 2) - (score_image.get_width() // 2), self.y))
