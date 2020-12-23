import pygame


class Game(object):
    BACKGROUND_COLOR = (0, 0, 255)

    def __init__(self, screen):
        # self.coordinate = True
        self.wait_to_start = True
        self.start = False
        self.false_start = False
        self.countdown = False
        self.start_countdown_time = 0
        self.screen = screen

    def restart_game(self):
        self.coordinate = True
        self.wait_to_start = True
        self.start = False
        self.false_start = False
        self.countdown = False
        self.start_countdown_time = 0

    def draw_board(self):
        self.screen.fill(self.BACKGROUND_COLOR)
        pygame.draw.rect(self.screen, (0, 0, 0), (50, 50, 1100, 700), 200, border_radius=350)
        pygame.draw.line(self.screen, (255, 255, 255), (600, 550), (600, 750), width=3)
        pygame.draw.line(self.screen, (255, 255, 255), (600, 600), (590, 600), width=3)
        pygame.draw.line(self.screen, (255, 255, 255), (600, 650), (590, 650), width=3)
        pygame.draw.line(self.screen, (255, 255, 255), (600, 700), (590, 700), width=3)
