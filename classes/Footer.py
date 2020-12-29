import pygame
from classes.Text import Text


class Footer(Text):
    def __init__(self, screen, font_name, font_size, players, color=(255, 255, 255)):
        super().__init__(screen, font_name, font_size, color)
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_xy_hidden = True
        self.players = players

    def update(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def draw(self):
        label_xy = f"x: {self.mouse_x}    y: {self.mouse_y}"
        label_keys = f"{self.players[0].name}: Left SHIFT,    {self.players[1].name}: Left ALT," \
                     f"    {self.players[2].name}: Right ALT,    {self.players[3].name}: Right SHIFT"
        if not self.mouse_xy_hidden:
            footer_label_xy = self.font.render(label_xy, True, self.color)
            footer_label_xy_rect = footer_label_xy.get_rect(x=10, y=770)
            self.screen.blit(footer_label_xy, footer_label_xy_rect)
        footer_label_keys = self.font.render(label_keys, True, self.color)
        footer_label_keys_rect = footer_label_keys.get_rect(x=250, y=770)
        self.screen.blit(footer_label_keys, footer_label_keys_rect)