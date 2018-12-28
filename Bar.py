import pygame
from Util import Util
from Coordinate import Coordinate

class Bar:

    def __init__(self):
        self.utility = Util()
        self.rect = pygame.Rect(200, 300, 80, 5)
        self.coordinate = Coordinate(0.0, 0.0, 0.0, 0.0)
        self.lives = 3
        self.score = 0

    def draw(self, DISPLAYSURF):
        #(x, y, width, height)
        pygame.draw.rect(DISPLAYSURF, self.utility.getColor("black"), self.rect)
        # draw lives to the screen
        self.drawLives(DISPLAYSURF)
        # draw score to the screen
        self.drawScore(DISPLAYSURF)

    def drawLives(self, DISPLAYSURF):
        # lives
        self.utility.draw_text(DISPLAYSURF, "Lives: " + str(self.lives), 25, 465, 390, "black", "white")

    def drawScore(self, DISPLAYSURF):
        # lives
        self.utility.draw_text(DISPLAYSURF, "Score: " + str(self.score), 25, 35, 390, "black", "white")

    def move(self, DISPLAYSURF, x):
        pygame.draw.rect(DISPLAYSURF, self.utility.getColor("white"), self.rect)
        if x > 0 and self.rect.x + x <= self.utility.getScreenWidth() - 80:
            self.rect.x = self.rect.x + x
        elif x < 0 and self.rect.x + x >= 0.0:
            self.rect.x = self.rect.x + x

        self.draw(DISPLAYSURF)

    def get_coordinate(self):
        self.coordinate.setCoordinates(self.rect.x, self.rect.y)
        return self.coordinate

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height

    def reduceLives(self):
        self.lives -= 1

    def getLives(self):
        return self.lives

    def updateScore(self, points):
        self.score = self.score + points
