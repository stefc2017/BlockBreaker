class Coordinate:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def setCoordinates(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)