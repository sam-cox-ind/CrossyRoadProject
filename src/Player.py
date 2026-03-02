import pygame

class Player:
    def __init__(self, screen: pygame.Surface, x, y, menu):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 30
        self.left_eye = (self.x - 8, self.y - 7)
        self.right_eye = (self.x + 8, self.y - 7)
        self.in_game = False
        self.menu = menu

    def draw(self):
        pygame.draw.circle(self.screen, self.menu.player_color, (self.x, self.y), 13)
        pygame.draw.circle(self.screen, "white", self.right_eye, 6)
        pygame.draw.circle(self.screen, "white", self.left_eye, 6)
        pygame.draw.circle(self.screen, "black", self.right_eye, 4)
        pygame.draw.circle(self.screen, "black", self.left_eye, 4)

    def move_left(self):
        self.x -= self.speed
        self.left_eye = (self.x - 7, self.y - 8)
        self.right_eye = (self.x - 7, self.y + 8)

    def move_right(self):
        self.x += self.speed
        self.left_eye = (self.x + 7, self.y + 8)
        self.right_eye = (self.x + 7, self.y - 8)

    def move_up(self):
        self.y -= self.speed
        self.left_eye = (self.x - 8, self.y - 7)
        self.right_eye = (self.x + 8, self.y - 7)

    def move_down(self):
        self.y += self.speed
        self.left_eye = (self.x - 8, self.y + 7)
        self.right_eye = (self.x + 8, self.y + 7)

    def pass_level(self):
        if self.y <= 13:
            return True
        else:
            return False

    def hit_by(self, obstacles):
        while self.in_game:
            hit_box = pygame.Rect(self.x - 13, self.y - 13, 26, 26)
            obstacle = pygame.Rect(obstacles.x, obstacles.y, obstacles.length, obstacles.height)
            return hit_box.colliderect(obstacle)
