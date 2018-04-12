import turtle

class Planet(object):
    def __init__(self, name, mass, distance, size, velocityX, velocityY, color):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.size = size
        self.velx = velocityX
        self.vely = velocityY
        self.color = color
        self.x = distance
        self.y = 0

        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.resizemode("user")
        self.pturtle.shapesize(self.size)
        self.pturtle.goto(self.x, self.y)
        self.pturtle.down()

    # Accessors - Getters
    def getName(self):
        return self.name

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velx

    def getYVel(self):
        return self.vely

    # Mutators
    def setXVel(self, newXVel):
        self.velx = newXVel

    def setYVel(self, newYVel):
        self.vely = newYVel

    def moveTo(self, newXPos, newYPos):
        self.x = newXPos
        self.y = newYPos
        self.pturtle.goto(newXPos, newYPos)

    











