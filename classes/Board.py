import pygame
from classes import Text


class Board(object):
    def __init__(self, screen, x, y, width, height, line_numbers, txt_color=(255, 208, 0), bkg_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bkg_color = bkg_color
        self.txt_color = txt_color
        self.screen = screen
        self.board_surface = pygame.Surface((self.width, self.height))
        self.board_rect = self.board_surface.get_rect(x=self.x, y=self.y)
        self.line_numbers = line_numbers
        self.lines = [Text.Text(self.board_surface, None, 40, color=self.txt_color) for _ in range(self.line_numbers)]

    def clear_board(self):
        for line in self.lines:
            line.set_text('')
        self.draw_board()

    def set_text_line(self, text, line_no):
        if line_no in range(1, self.line_numbers + 1):
            self.lines[line_no-1].set_text(text)

    def set_line_txt_color(self, color, line_no):
        if line_no in range(1, self.line_numbers+1):
            self.lines[line_no-1].set_color(color)

    def draw_board(self):
        self.board_surface.fill(self.bkg_color)
        h = self.board_rect.height
        line_h = int(h/self.line_numbers)
        for index, lines in enumerate(self.lines):
            lines.draw_centered((self.board_surface.get_width()/2, index * line_h + line_h/2))
        self.screen.blit(self.board_surface, self.board_rect)

