import pygame, sys
from pygame.locals import *


class Util:

    def __init__(self):
        colors = dict()
        colors["white"] = (255, 255, 255)
        colors["green"] = (0, 255, 0)
        colors["blue"] = (0, 0, 128)
        colors["black"] = (0, 0, 128)
        colors["red"] = (255, 0, 0)

        self.colors = colors
        self.fps = 30
        self.screenWidth = 500
        self.screenHeight = 400
        self.blockWidth = 50
        self.blockHeight = 50
        self.blockRows = 3
        self.blockCols = 10

    def draw_text(self, DISPLAYSURF, text, font_size, x_coor, y_coor, color_text, color_box):
        fontObj = pygame.font.SysFont('courier header', font_size)
        textSurfaceObj = fontObj.render(text, True, self.colors[color_text], self.colors[color_box])
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (x_coor, y_coor)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    def getColor(self, color):
        return self.colors[color]

    def getFPS(self):
        return self.fps

    def getScreenWidth(self):
        return self.screenWidth

    def getScreenHeight(self):
        return self.screenHeight

    def getBlockHeight(self):
        return self.blockHeight

    def getBlockWidth(self):
        return self.blockWidth

    def getNumOfBlockRows(self):
        return self.blockRows

    def getNumOfBlockCols(self):
        return self.blockCols

    def getBallNBlockCollision(self, ball, blocks):
        ballX = ball.getX()
        ballY = ball.getY()
        collision = None

        for row in range(0, self.getNumOfBlockRows()):
            for col in range(0, self.getNumOfBlockCols()):
                if (row,col) in blocks.keys():
                    block_coordinate = blocks[row, col].getCoordinate()
                    blockX = block_coordinate.getX()
                    blockY = block_coordinate.getY()

                    if ballX in range(blockX, blockX + self.blockWidth) and ballY in range(blockY, blockY + self.blockHeight):
                        collision = blocks[row, col]
                        break
        return collision


