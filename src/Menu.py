import pygame


class Menu:
    def __init__(self, screen, title, button_name, start_menu):
        self.screen = screen
        self.width = self.screen.get_width() - 60
        self.height = self.screen.get_height() - 200
        self.x = (self.screen.get_width() // 2) - (self.width // 2)
        self.y = (self.screen.get_height() // 2) - (self.height // 2)
        self.start_menu = start_menu

        self.title_font = pygame.font.Font(None, 70)
        self.title = title
        self.title_image = self.title_font.render(self.title, True, (255, 255, 255))
        self.title_x = self.x + (self.width // 2) - (self.title_image.get_width() // 2)
        self.title_y = self.y + 20

        self.play_font = pygame.font.Font(None, 40)
        self.play = button_name
        self.play_image = self.play_font.render(self.play, True, (255, 255, 255))
        self.play_x = self.x + (self.width // 2) - (self.play_image.get_width() // 2)
        self.play_y = self.y + self.height - 50
        self.play_button_x = self.play_x - 10
        self.play_button_y = self.play_y - 5
        self.play_button_width = self.play_image.get_width() + 20
        self.play_button_height = self.play_image.get_height() + 10

        self.green_player_x = self.x + (self.width // 4)
        self.red_player_x = self.x + (self.width // 2)
        self.blue_player_x = self.x + (3 * self.width // 4)
        self.player_y = self.y + 150

        self.green_player_left_eye = (self.green_player_x - 24, self.player_y - 21)
        self.green_player_right_eye = (self.green_player_x + 24, self.player_y - 21)
        self.red_player_left_eye = (self.red_player_x - 24, self.player_y - 21)
        self.red_player_right_eye = (self.red_player_x + 24, self.player_y - 21)
        self.blue_player_left_eye = (self.blue_player_x - 24, self.player_y - 21)
        self.blue_player_right_eye = (self.blue_player_x + 24, self.player_y - 21)

        self.player_selected_x = self.green_player_x
        self.player_selected_y = self.player_y + 80

        self.player_color = "green"

        self.instructions_font = pygame.font.Font(None, 40)
        self.instructions = "Use Arrow Keys To Move"
        self.instructions_image = self.instructions_font.render(self.instructions, True, (255, 255, 255))
        self.instructions_x = self.x + (self.width // 2) - (self.instructions_image.get_width() // 2)
        self.instructions_y = self.y + self.height - 140

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        self.screen.blit(self.title_image, (self.title_x, self.title_y))

        pygame.draw.rect(self.screen, (100, 100, 100), (self.play_button_x, self.play_button_y, self.play_button_width, self.play_button_height))
        self.screen.blit(self.play_image, (self.play_x, self.play_y))

        if self.start_menu:
            pygame.draw.circle(self.screen, "green", (self.green_player_x, self.player_y), 39)
            pygame.draw.circle(self.screen, "red", (self.red_player_x, self.player_y), 39)
            pygame.draw.circle(self.screen, "blue", (self.blue_player_x, self.player_y), 39)
            pygame.draw.circle(self.screen, "white", self.green_player_left_eye, 18)
            pygame.draw.circle(self.screen, "white", self.green_player_right_eye, 18)
            pygame.draw.circle(self.screen, "black", self.green_player_left_eye, 12)
            pygame.draw.circle(self.screen, "black", self.green_player_right_eye, 12)
            pygame.draw.circle(self.screen, "white", self.red_player_left_eye, 18)
            pygame.draw.circle(self.screen, "white", self.red_player_right_eye, 18)
            pygame.draw.circle(self.screen, "black", self.red_player_left_eye, 12)
            pygame.draw.circle(self.screen, "black", self.red_player_right_eye, 12)
            pygame.draw.circle(self.screen, "white", self.blue_player_left_eye, 18)
            pygame.draw.circle(self.screen, "white", self.blue_player_right_eye, 18)
            pygame.draw.circle(self.screen, "black", self.blue_player_left_eye, 12)
            pygame.draw.circle(self.screen, "black", self.blue_player_right_eye, 12)

            pygame.draw.circle(self.screen, "green", (self.player_selected_x, self.player_selected_y), 12)
            pygame.draw.line(self.screen, "white", (self.player_selected_x - 8, self.player_selected_y), (self.player_selected_x - 4, self.player_selected_y + 6), 4)
            pygame.draw.line(self.screen, "white", (self.player_selected_x - 4, self.player_selected_y + 6), (self.player_selected_x + 6, self.player_selected_y - 6), 4)

            self.screen.blit(self.instructions_image, (self.instructions_x, self.instructions_y))

        if not self.start_menu:
            pygame.draw.circle(self.screen, self.player_color, (self.red_player_x, self.player_y), 39)
            pygame.draw.circle(self.screen, "white", self.red_player_left_eye, 18)
            pygame.draw.circle(self.screen, "white", self.red_player_right_eye, 18)
            pygame.draw.line(self.screen, "black", (self.red_player_x - 31, self.player_y - 28),
                             (self.red_player_x - 17, self.player_y - 14), 7)
            pygame.draw.line(self.screen, "black", (self.red_player_x - 31, self.player_y - 14),
                             (self.red_player_x - 17, self.player_y - 28), 7)
            pygame.draw.line(self.screen, "black", (self.red_player_x + 31, self.player_y - 28),
                             (self.red_player_x + 17, self.player_y - 14), 7)
            pygame.draw.line(self.screen, "black", (self.red_player_x + 31, self.player_y - 14),
                             (self.red_player_x + 17, self.player_y - 28), 7)

    def on_play_button(self):
        click_x, click_y = pygame.mouse.get_pos()
        if click_x > self.play_button_x and click_x < (self.play_button_x + self.play_button_width) and click_y > self.play_button_y and click_y < (self.play_button_y + self.play_button_height):
            return True
        return False

    def on_green_player(self):
        click_x, click_y = pygame.mouse.get_pos()
        if click_x > self.green_player_x - 45 and click_x < self.green_player_x + 45 and click_y > self.player_y - 45 and click_y < self.player_y + 45:
            return True
        return False

    def on_red_player(self):
        click_x, click_y = pygame.mouse.get_pos()
        if click_x > self.red_player_x - 45 and click_x < self.red_player_x + 45 and click_y > self.player_y - 45 and click_y < self.player_y + 45:
            return True
        return False

    def on_blue_player(self):
        click_x, click_y = pygame.mouse.get_pos()
        if click_x > self.blue_player_x - 45 and click_x < self.blue_player_x + 45 and click_y > self.player_y - 45 and click_y < self.player_y + 45:
            return True
        return False
