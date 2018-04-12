import turtle, random


class Fish(object):
    def __init__(self):
        self.fturtle = turtle.Turtle()
        self.fturtle.up()
        self.fturtle.hideturtle()
        # the shape of the turtle object must also be registered
        # with the world class
        self.fturtle.shape("Fish.gif")

        self.xpos = 0
        self.ypos = 0
        self.world = None
        self.breedTick = 0

    def setX(self, newx):
        self.xpos = newx

    def setY(self, newy):
        self.ypos = newy

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def setWorld(self, aworld):
        self.world = aworld

    def appear(self):
        self.fturtle.goto(self.xpos, self.ypos)
        self.fturtle.showturtle()

    def hide(self):
        self.fturtle.hideturtle()

    def move(self, newx, newy):
        self.world.moveLifeForm(self.xpos, self.ypos, newx, newy)
        self.xpos = newx
        self.ypos = newy
        self.fturtle.goto(self.xpos, self.ypos)

    def tryToMove(self):
        newLocation = self._getOffsetLocation()

        if self.world.emptyLocation(newLocation[0], newLocation[1]):
            self.move(newLocation[0], newLocation[1])

    def _getOffsetLocation(self):
        offsetList = [(-1, 1), (0, 1), (1, 1),
                      (-1, 0)        , (1, 0),
                      (-1, -1), (0, -1), (1, -1)]
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        newx = self.xpos + randomOffset[0]
        newy = self.ypos + randomOffset[1]
        # Location must be valid
        while not (0 <= newx < self.world.getMaxX() and
                   0 <= newy < self.world.getMaxY()):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            newx = self.xpos + randomOffset[0]
            newy = self.ypos + randomOffset[1]

        return newx, newy

    def tryToBreed(self):
        newLocation = self._getOffsetLocation()

        if self.world.emptyLocation(newLocation[0], newLocation[1]):
            child = Fish()
            self.world.addLifeForm(child, newLocation[0], newLocation[1])
            self.breedTick = 0

    def liveALittle(self):
        offsetList = [(-1, 1), (0, 1), (1, 1),
                        (-1, 0)      , (1, 0),
                        (-1, -1), (0, -1), (1, -1)]
        adjfish = 0
        for offset in offsetList:
            newx = self.xpos + offset[0]
            newy = self.ypos + offset[1]
            if 0 <= newx < self.world.getMaxX() and \
                    0 <= newy < self.world.getMaxY():
                if (not self.world.emptyLocation(newx, newy)) and \
                        isinstance(self.world.lookAtLocation(newx, newy), Fish):
                    adjfish += 1

        if adjfish >= 2:
            self.world.delLifeForm(self)
        else:
            self.breedTick += 1
            if self.breedTick >= 12:
                self.tryToBreed()
            self.tryToMove()






