import pygame
from classes.Math import Vec2D

class Truck (object):
    def __init__(self, oval_width, oval_height, truck_width, bkg_color):
        self.width = oval_width
        self.height = oval_height
        self.truck_width = truck_width
        self.bkg_color = bkg_color
        self.arc_radius = self.height/2 - self.truck_width/2
        self.arcs_centers = self.calculate_arcs_centers()
        # self.right_arc_center = self.get_arc_center("right")

    def draw_truck(self):
        truck = pygame.Surface((self.width, self.height))
        truck.fill(self.bkg_color)
        truck_rect = pygame.draw.rect(truck, (0, 0, 0), (self.truck_width/2, self.truck_width/2, self.width - self.truck_width, self.height - self.truck_width),self.truck_width)
        truck.blit(truck, truck_rect)
        return truck

    def calculate_arcs_centers(self):
        y = self.height/2
        left_x = self.truck_width/2 + self.arc_radius
        right_x = self.width - self.truck_width/2 - self.arc_radius
        return ((left_x, y), (right_x, y))
