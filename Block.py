import pygame
from Util import Util
import time

class Block:

    def __init__(self, index_r, index_c, health, color, coordinate, points):
        self.index_r = index_r
        self.index_c = index_c
        self.health = health
        self.remaining_health = health
        self.points = points
        self.color = color
        self.utility = Util()
        self.coordinate = coordinate

    def draw(self, DISPLAYSURF):
        # (x, y, width, height)
        block = pygame.Rect(self.coordinate.getX(), self.coordinate.getY(),
                            self.coordinate.getWidth(), self.coordinate.getHeight())
        pygame.draw.rect(DISPLAYSURF, self.utility.getColor(self.color), block)

    def getCoordinate(self):
        return self.coordinate

    def getIndexRow(self):
        return self.index_r

    def getIndexCol(self):
        return self.index_c

    def getHealth(self):
        return self.health

    def deductHealth(self, blocks, ball, player, DISPLAYSURF):
        self.remaining_health = self.remaining_health - 1
        blocks[self.getIndexRow(), self.getIndexCol()] = self

        if self.remaining_health <= 0:
            player.updateScore(self.getPoints())
            self.color = "white"
            del blocks[self.getIndexRow(), self.getIndexCol()]
            self.draw(DISPLAYSURF)
            ball.inverseUpdateX()
        else:
            ball.inverseUpdateY()

        return blocks

    def getPoints(self):
        return self.points

    def toString(self):
        return "row: " + str(self.index_r) + ", col: " + str(self.index_c)
