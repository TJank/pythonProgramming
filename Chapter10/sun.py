import math
import turtle


class Sun:
    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    def getXPos(self):
        return self.x
    def getYPos(self):
        return self.y

    def getMass(self):
        return self.mass

    def __str__(self):
        return self.name

    def getTemperature(self):
        return self.temp

    def getVolume(self):
        v = 4 / 3 * math.pi * self.radius ** 3
        return v

    def getSurfaceArea(self):
        sa = 4 * math.pi * self.radius ** 2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def setName(self, newname):
        self.name = newname

    def getRadius(self):
        return self.radius