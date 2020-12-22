import pygame


class Player(object):
    def __init__(self, name, pool):
        self.name = name
        self.x = 600
        if pool == 1:
            self.y = 575
            self.color = (255, 0, 0)
        elif pool == 2:
            self.y = 625
            self.color = (238, 238, 0)
        elif pool == 3:
            self.y = 675
            self.color = (0, 0, 255)
        else:
            self.y = 725
            self.color = (255, 255, 255)
        self.v = 1

    def draw_player(self, surface):
        pygame.draw.line(surface, self.color, (self.x-30, self.y), (self.x, self.y), width=3)