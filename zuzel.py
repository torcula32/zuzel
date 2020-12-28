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

players = [Player(f"Player{x}", x, screen) for x in range(1, 5)]

speedway = Game(screen, players)
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
            if speedway.false_start:
                speedway.false_start = False
                speedway.wait_to_start = True
            if speedway.countdown:
                if (event.key == K_LCTRL and players[0].false_start == False)\
                        or (event.key == K_LALT and players[1].false_start == False)\
                        or (event.key == K_RALT and players[2].false_start == False)\
                        or (event.key == K_RSHIFT and players[3].false_start == False):
                    speedway.false_start = True
                    speedway.countdown = False
                    if event.key == K_LCTRL:
                        players[0].false_start = True
                    elif event.key == K_LALT:
                        players[1].false_start = True
                    elif event.key == K_RALT:
                        players[2].false_start = True
                    else:
                        players[3].false_start = True
            if speedway.start:                  #TODO: change to checking key status instead of key event
                if event.key == K_LCTRL and players[0].false_start == False:
                    players[0].change_alpha()
                if event.key == K_LALT and players[1].false_start == False:
                    players[1].change_alpha()
                if event.key == K_RALT and players[2].false_start == False:
                    players[2].change_alpha()
                if event.key == K_RSHIFT and players[3].false_start == False:
                    players[3].change_alpha()
    if speedway.start:
        for player in players:
            if not player.stop:
                player.move()
                player.update()
                player.check_collision()
    if players[0].false_start and players[1].false_start and players[2].false_start and players[3].false_start:
        speedway.restart_game()
    x, y = pygame.mouse.get_pos()
    footer.update(x, y)
    speedway.draw_board()
    for player in players:
        if not player.false_start:
            player.draw_player()
    if speedway.wait_to_start:
        center.set_text("Press any key to start...")
        center.set_color((255, 255, 255))
    if speedway.false_start:
        center.set_text("False start !!!")
        center.set_color((255, 0, 0))
    if speedway.countdown:
        count_label = ""
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
            speedway.countdown = False
        center.set_text(count_label)
    center.draw_centered()
    footer.draw()
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
sys.exit()
