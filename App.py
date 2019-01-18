import pygame
import sys
import time

from Ball import Ball
from Bar import Bar
from Block import Block
from Coordinate import Coordinate
from Util import Util
from pygame.locals import *

def main():
    pygame.init()
    utility = Util()

    DISPLAYSURF = pygame.display.set_mode((utility.getScreenWidth(), utility.getScreenHeight()))
    DISPLAYSURF.fill(utility.getColor("white"))
    pygame.display.set_caption('Demo!')

    load_main_screen(utility, DISPLAYSURF)
    play_game(utility, DISPLAYSURF)


def play_game(utility, DISPLAYSURF):
    fps_clock = pygame.time.Clock()

    pygame.mixer.music.load("./music/game_theme.mp3")
    pygame.mixer.music.play(-1, 2.0)

    player = Bar()
    ball = Ball()

    player.draw(DISPLAYSURF)
    ball.draw(DISPLAYSURF)
    blocks = draw_blocks(utility, DISPLAYSURF)

    while True: # main game loop
        keys = pygame.key.get_pressed()

        #move bar when right or left arrow is held down or pushed down
        if(keys[pygame.K_RIGHT]):
            player.move(DISPLAYSURF, 3)
        elif(keys[pygame.K_LEFT]):
            player.move(DISPLAYSURF, -3)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                print(event.pos)

        ball.move(DISPLAYSURF, player)
        draw_blocks2(utility, DISPLAYSURF, blocks)
        # determine if ball hits a block
        block_collision = utility.getBallNBlockCollision(ball, blocks)

        if block_collision:
            # deduct from that blocks health
            blocks = block_collision.deductHealth(blocks, ball, player, DISPLAYSURF)

        if ball.outOfScreen():
            player.reduceLives()
            ball.resetPosition()

        pygame.display.update()
        fps_clock.tick(utility.getFPS())


def load_main_screen(utility, DISPLAYSURF):
    doesnt_want_to_play = True
    current_coors = Coordinate(0.0, 0.0, 0.0, 0.0)

    pygame.mixer.music.load("./music/main_theme.mp3")
    pygame.mixer.music.play(-1, 0.0)

    #title
    utility.draw_text(DISPLAYSURF, "GAME DEMO", 50, 235, 100, "green", "white")
    #play
    utility.draw_text(DISPLAYSURF, "PLAY", 25, 225, 300, "green", "black")

    while doesnt_want_to_play: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                x, y = event.pos
                current_coors.setCoordinates(x, y)
                #clicked play
                if current_coors.getX() in range(166, 284) and current_coors.getY() in range(290, 309):
                    doesnt_want_to_play = False
                    pygame.mixer.music.stop()
                    DISPLAYSURF.fill(utility.getColor("white"))
                    time.sleep(0.1)
        pygame.display.update()


def draw_blocks(utility, DISPLAYSURF):
    blocks = initialize_blocks(utility)
    for row in range(0, utility.getNumOfBlockRows()):
        for col in range(0, utility.getNumOfBlockCols()):
            blocks[row, col].draw(DISPLAYSURF)
    return blocks

def draw_blocks2(utility, DISPLAYSURF, blocks):
    for row in range(0, utility.getNumOfBlockRows()):
        for col in range(0, utility.getNumOfBlockCols()):
            if (row, col) in blocks.keys():
                blocks[row, col].draw(DISPLAYSURF)

def initialize_blocks(utility):
    x = 0
    y = -utility.getBlockWidth()
    width = utility.getBlockWidth()
    height = utility.getBlockHeight()
    blocks = dict()
    point = 1

    for row in range(0, utility.getNumOfBlockRows()):
        x = 0
        y += height
        for col in range(0, utility.getNumOfBlockCols()):
            color = change_color(point)
            blocks[row, col] = Block(row, col, point, color,
                                     Coordinate(x, y, width, height), point)
            x += width
            point = update_point(point)

    return blocks


def update_point(point):
    if point == 3:
        point = 1
    else:
        point += 1
    return point


def change_color(point):
    current_color = "white" # default

    if point == 1:
        current_color = "red"
    elif point == 2:
        current_color = "green"
    elif point == 3:
        current_color = "blue"

    return current_color


main()
