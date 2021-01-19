import pygame


class Text(object):
    def __init__(self, screen, font_name=None, font_size=20, text='', color=(255, 255, 255)):
        if font_name is None:
            self.font = pygame.font.Font('fonts/belfast/belfast.ttf', font_size)
        else:
            self.font = pygame.font.SysFont(font_name, font_size)
        self.x = 0
        self.y = 0
        self.screen = screen
        self.text = text
        self.color = color

    def set_text(self, text):
        self.text = text

    def set_color(self, color):
        self.color = color

    def draw_centered(self, center):
        center_label = self.font.render(self.text, True, self.color)
        center_label_rect = center_label.get_rect(center=center)
        self.screen.blit(center_label, center_label_rect)
