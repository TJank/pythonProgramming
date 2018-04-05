import math
import turtle
class Planet:
    def __init__(self, iname, irad, im, idist, ic):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.x = idist
        self.y = 0
        self.color = ic
        #self.numMoons = moons
        #self.moonList = []

        self.pturtle = turtle.Turtle()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")

        self.pturtle.up()
        self.pturtle.goto(self.x,self.y)
        self.pturtle.down()

    def getXPos(self):
        return self.x
    def getYPos(self):
        return self.y

    # Listing 10.2 Acessor Methods pg 336
    def getName(self):
        return self.name
    def getRadius(self):
        return self.radius
    def getMass(self):
        return self.mass
    def getDistance(self):
        return self.distance

    # def getMoons(self):
    #     return self.numMoons

    # Listing 10.3 pg 337
    def getCircumference(self):
        c = 2 * math.pi * self.radius
        return c

    def getVolume(self):
        v = 4/3 * math.pi * self.radius**3
        return v

    def getSurfaceArea(self):
        sa = 4 * math.pi * self.radius**2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def show(self):
        print(self.name)

    def __str__(self):
        return self.name

    # MUTATOR Methods
    def setName(self, newname):
        self.name = newname

    # def setMoons(self, num_new_moons):
    #     self.numMoons = self.numMoons + num_new_moons
    #
    # def addMoon(self, moon_name):
    #     self.moonList.append(moon_name)