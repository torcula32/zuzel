import sys
import time
import pygame
from pygame.locals import *
from classes.Game import Game
from classes.Player import Player
from classes.Text import Text
from classes.Footer import Footer

FPS = 30
WINDOW_SIZE = (1200, 800)

pygame.init()
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Zuzel by Tommy")

players = [Player(f"Player{x}", x) for x in range(1, 5)]

speedway = Game(screen)
speedway.draw_board()
footer = Footer(screen, "Arial", 20, players)
center = Text(screen, "Comic Sans MS", 58)

run = True

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_BACKQUOTE:
                footer.mouse_xy_hidden = not footer.mouse_xy_hidden
            if speedway.wait_to_start:
                speedway.wait_to_start = False
                speedway.countdown = True
                speedway.start_countdown_time = time.time()
            if speedway.countdown:
                if event.key == K_LCTRL or event.key == K_LALT or event.key == K_RALT or event.key == K_RSHIFT:
                    speedway.false_start = True
                    speedway.countdown = False
    x, y = pygame.mouse.get_pos()
    footer.update(x, y)
    speedway.draw_board()
    for player in players:
        player.draw_player(screen)
    if speedway.wait_to_start:
        center.set_text("Press any key to start...")
    if speedway.false_start:
        center.set_text("False start !!!")
        center.set_color((255, 0, 0))
    if speedway.countdown:
        if time.time() - speedway.start_countdown_time <= 1:
            count_label = "4"
        elif time.time() - speedway.start_countdown_time <= 2:
            count_label = "3"
        elif time.time() - speedway.start_countdown_time <= 3:
            count_label = "2"
        elif time.time() - speedway.start_countdown_time <= 4:
            count_label = "1"
        elif time.time() - speedway.start_countdown_time > 4:
            count_label = "Go"
            speedway.start = True
        center.set_text(count_label)
    center.draw_centered()
    footer.draw()
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
sys.exit()
