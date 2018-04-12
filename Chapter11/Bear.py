import turtle
import random
from Fish import Fish


class Bear(object):
    def __init__(self):
        self.bturtle = turtle.Turtle()
        self.bturtle.up()
        self.bturtle.hideturtle()
        self.bturtle.shape("Bear.gif")    # will only work if the file name is also
                                          # registered with the World class
        self.xpos = 0
        self.ypos = 0
        self.world = None
        self.breedTick = 0
        self.starveTick = 0

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

    def hide(self):
        self.bturtle.hideturtle()

    def appear(self):
        self.bturtle.goto(self.xpos, self.ypos)
        self.bturtle.showturtle()

    def move(self, newx, newy):
        self.world.moveLifeForm(self.xpos, self.ypos, newx, newy)
        self.xpos = newx
        self.ypos = newy
        self.bturtle.goto(self.xpos, self.ypos)

    def _getOffsetLocation(self):
        offset = [(-1, 1), (0, 1), (1, 1),
                  (-1, 0), (1, 0),
                  (-1, -1), (0, -1), (1, -1)]

        randomOffsetIndex = random.randrange(len(offset))
        randomOffset = offset[randomOffsetIndex]

        # randomOffset = random.choice(offset)

        newx = self.xpos + randomOffset[0]
        newy = self.ypos + randomOffset[1]
        # check if location is valid
        locationIsValid = (0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY())
        while (not locationIsValid):
            randomOffsetIndex = random.randrange(len(offset))
            randomOffset = offset[randomOffsetIndex]
            newx = self.xpos + randomOffset[0]
            newy = self.ypos + randomOffset[1]

        return newx, newy

    def tryToMove(self):
        newLocation = self._getOffsetLocation()

        # check if location is empty
        if self.world.emptyLocation(newLocation[0], newLocation[1]):
            self.move(newLocation[0], newLocation[1])

    def tryToBreed(self):
        newLocation = self._getOffsetLocation()

        # check if location is empty
        if self.world.emptyLocation(newLocation[0], newLocation[1]):
            child = Bear()
            self.world.addLifeForm(child, newLocation[0], newLocation[1])

    def tryToEat(self):
        newLocation = self._getOffsetLocation()

        if (not self.world.emptyLocation(newLocation[0], newLocation[1]) and \
            isinstance(self.world.lookAtLocation(newLocation[0], newLocation[1]), Fish)):
            self.world.delLifeForm(self.world.lookAtLocation(newLocation[0], newLocation[1]))
            self.move(newLocation[0], newLocation[1])
            self.starveTick = 0
        else:
            self.starveTick += 1


    def liveALittle(self):  # take a turn
        self.breedTick += 1
        if self.breedTick >= 8:
            self.tryToBreed()

        self.tryToEat()

        if self.starveTick == 10:
            self.world.delLifeForm(self)
        else:
            self.tryToMove()














































