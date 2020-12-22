import sys
import pygame
from pygame.locals import *
from classes.Player import Player

FPS = 30
WINDOW_SIZE = (1200, 800)
BACKGROUND_COLOR = (0, 0, 255)
coordinate = False
start = False

pygame.init()
pygame.font.init()
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Zuzel by Tommy")

# font = pygame.font.Font("Arial", 20)
font = pygame.font.SysFont("Arial", 20)
player1 = Player("Player1", 1)
player2 = Player("Player2", 2)
player3 = Player("Player3", 3)
player4 = Player("Player4", 4)


truck = pygame.Surface((WINDOW_SIZE[0]-100, WINDOW_SIZE[1]-100))
truck.fill(BACKGROUND_COLOR)
truck_rect = truck.get_rect(x=50 ,y=50)
# pygame.draw.ellipse(truck, (0, 0, 0), truck_rect)
pygame.draw.rect(truck, (0, 0, 0), (0, 0, 1100, 700), 200, border_radius=350)
pygame.draw.line(truck, (255, 255, 255), (550, 500), (550, 700), width=3)
pygame.draw.line(truck, (255, 255, 255), (550, 550), (540, 550), width=3)
pygame.draw.line(truck, (255, 255, 255), (550, 600), (540, 600), width=3)
pygame.draw.line(truck, (255, 255, 255), (550, 650), (540, 650), width=3)

screen.fill(BACKGROUND_COLOR)
screen.blit(truck, truck_rect)

run = True

while run:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(truck, truck_rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_BACKQUOTE:
                coordinate = not coordinate
    x, y = pygame.mouse.get_pos()
    label = f"x: {x}, y: {y}"
    coordinate_label = font.render(label, True, (255, 255, 255))
    coordinate_label_rect = coordinate_label.get_rect(x=100, y=770)
    screen.fill(BACKGROUND_COLOR)
    screen.blit(truck, truck_rect)
    player1.draw_player(screen)
    player2.draw_player(screen)
    player3.draw_player(screen)
    player4.draw_player(screen)
    if coordinate:
        screen.blit(coordinate_label, coordinate_label_rect)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
sys.exit()