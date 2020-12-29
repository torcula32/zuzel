import pygame
import math
import logging
from pygame import Color
from pygame.locals import *
from classes.Game import Game


class Player(object):
    pool_colors = [(255, 0, 0), (238, 238, 0), (0, 0, 255), (255, 255, 255)]
    pool_y = [575, 625, 675, 725]
    keys = [K_LSHIFT, K_LALT, K_RALT, K_RSHIFT]
    end_lap_rect = pygame.rect.Rect(600, 550, 30, 200)

    def __init__(self, name, pool, surface):
        self.name = name
        self.x = 600
        self.pool = pool
        self.y = self.pool_y[self.pool-1]
        self.color = self.pool_colors[self.pool-1]
        self.v = 1.0
        self.lap = 0
        self.player_points = self.init_points()
        self.false_start = False
        self.stop = False
        self.surface = surface
        self.alpha = 0
        self.step_v = 0.3
        self.step_a = 5
        self.key = self.keys[self.pool-1]
        self.player_points_max_lenght = 40
        self.player_points_min_lenght = 10
        self.inside_end_area = True
        self.crash = False

    def init_points(self):
        points = [(self.x - 30, self.y), (self.x, self.y)]
        return points

    def draw_player(self):
        xs, ys = self.player_points[0]
        for x, y in self.player_points[1:]:
            pygame.draw.line(self.surface, self.color, (xs, ys), (x, y), width=3)
            xs, ys = x, y

    def update(self):
        self.player_points.append((self.x, self.y))
        if len(self.player_points) >= self.player_points_max_lenght:
            self.player_points.pop(0)

    def move(self):
        if pygame.key.get_pressed()[self.key]:
            if self.alpha == 0:
                self.alpha = 360
            self.alpha -= self.step_a
            if self.v > 1.0:
                self.v -= self.step_v
            if len(self.player_points) <= self.player_points_min_lenght:
                self.player_points.pop(0)
        else:
            self.v += self.step_v
        self.x = int(self.x + self.v * math.cos((self.alpha * math.pi)/180))
        self.y = int(self.y + self.v * math.sin((self.alpha * math.pi)/180))
        self.update()
        if self.name == "Player2":
            logging.warning(f"Player: {self.name}, lap: {self.lap}, x: {self.x}, y: {self.y}, v: {self.v}, alpha: {self.alpha}")
            logging.warning(f"Player: {self.name}, pos[]: {self.player_points}")

    def change_alpha(self):
        if self.alpha == 0:
            self.alpha = 360
        self.alpha -= 5

    def check_collision(self):
        if self.surface.get_at((self.x, self.y)) == Color(Game.BACKGROUND_COLOR):
            self.stop = True
            self.crash = True
        if self.end_lap_rect.collidepoint(self.x, self.y):
            if not self.inside_end_area:
                self.lap += 1
                self.inside_end_area = True
                if self.lap > 4:
                    self.stop = True
        else:
            if self.inside_end_area:
                self.inside_end_area = False
#TODO: add check laps end
    def player_restore(self):
        self.x = 600
        self.y = self.pool_y[self.pool-1]
        self.v = 1.0
        self.lap = 0
        self.player_points = self.init_points()
        self.false_start = False
        self.stop = False
        self.alpha = 0
        self.inside_end_area = True
        self.crash = False

