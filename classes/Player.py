import pygame
import math
from pygame import Color
from classes.Game import Game


class Player(object):
    pool_colors = [(255, 0, 0), (238, 238, 0), (0, 0, 255), (255, 255, 255)]
    pool_y = [575, 625, 675, 725]

    def __init__(self, name, pool, surface):
        self.name = name
        self.x = 600
        self.pool = pool
        self.y = self.pool_y[pool-1]
        self.color = self.pool_colors[pool-1]
        self.v = 1.0
        self.lap = 0
        self.player_points = self.init_points()
        self.false_start = False
        self.stop = False
        self.surface = surface
        self.alpha = 0

    def init_points(self):
        points = []
        points.append((self.x - 30, self.y))
        points.append((self.x, self.y))
        return points

    def draw_player(self):
        xs, ys = self.player_points[0]
        for x, y in self.player_points[1:]:
            pygame.draw.line(self.surface, self.color, (xs, ys), (x, y), width=3)
            xs, ys = x, y

    def update(self):
        self.player_points.append((self.x, self.y))

    def move(self):
        self.x = int(self.x + self.v * math.cos((self.alpha * math.pi)/180))
        self.v += 1
        self.y = int(self.y + self.v * math.sin((self.alpha * math.pi)/180))

    def change_alpha(self):
        if self.alpha == 0:
            self.alpha = 360
        self.alpha -= 5

    def check_collision(self):
        if self.surface.get_at((self.x, self.y)) == Color(Game.BACKGROUND_COLOR):
            self.stop = True
