import pygame


class Player(object):
    pool_colors = [(255, 0, 0), (238, 238, 0), (0, 0, 255), (255, 255, 255)]
    pool_y = [575, 625, 675, 725]

    def __init__(self, name, pool):
        self.name = name
        self.x = 600
        self.pool = pool
        self.y = self.pool_y[pool-1]
        self.color = self.pool_colors[pool-1]
        self.v = 0
        self.laps = 0

    def draw_player(self, surface):
        pygame.draw.line(surface, self.color, (self.x-30, self.y), (self.x, self.y), width=3)

    def update(self):
        pass
