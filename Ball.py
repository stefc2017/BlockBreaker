import pygame
import time
from Util import Util
from Bar import Bar
from Coordinate import Coordinate


class Ball:

    def __init__(self):
        self.utility = Util()
        self.x = 100
        self.y = 200
        self.updateX = 2
        self.updateY = 2
        self.lives = 3
        self.radius = 5
        self.thickness = 5

    def draw(self, DISPLAYSURF):
        # (screen, color, (x,y), radius, thickness)
        pygame.draw.circle(DISPLAYSURF, self.utility.getColor("black"), (self.x, self.y), self.radius, self.thickness)

    def move(self, DISPLAYSURF, player):
        pygame.draw.circle(DISPLAYSURF, self.utility.getColor("white"), (self.x, self.y), self.radius, self.thickness)
        player_coords = player.get_coordinate()
        player_x = player_coords.getX()
        player_y = player_coords.getY()
        player_width = player.get_width()
        player_height = player.get_height()

        if self.x + self.updateX >= self.utility.getScreenWidth():  # right side
            self.updateX = -2
            self.x = self.x + self.updateX
            self.y = self.y + self.updateY
        elif self.x + self.updateX <= 0:  # left side
            self.updateX = 2
            self.x = self.x + self.updateX
            self.y = self.y + self.updateY
        elif (self.y + self.updateY) in range(player_y, player_y + player_height) \
                and (self.x + self.updateY) in range(player_x, player_x + player_width + 1):  # bar
            self.updateY = -2
            self.x = self.x + self.updateX
            self.y = self.y + self.updateY
        elif self.y + self.updateY <= 0:  # top
            self.updateY = 2
            self.x = self.x + self.updateX
            self.y = self.y + self.updateY
        else:
            self.x += self.updateX
            self.y += self.updateY

        self.draw(DISPLAYSURF)
        player.draw(DISPLAYSURF)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def inverseUpdateY(self):
        self.updateY = -self.updateY

    def inverseUpdateX(self):
        self.updateX = -self.updateX

    def outOfScreen(self):
        if self.y > self.utility.getScreenHeight() + self.radius + 1:
            return True

    def resetPosition(self):
        time.sleep(2)
        self.x = 100
        self.y = 200
        self.updateX = 2
        self.updateY = 2

