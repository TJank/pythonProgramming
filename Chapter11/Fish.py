import turtle, random

class Fish(object):
    def __init__(self):
        self.fturtle = turtle.Turtle()
        self.fturtle.up()
        self.fturtle.hideturtle()
        self.fturtle.shape("Fish.gif")  # will only work if the file name has been registered in the World class

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

    def appear(self):
        self.fturtle.goto(self.xpos, self.ypos)
        self.fturtle.showturtle()

    def hide(self):
        self.fturtle.hideturtle()

    def move(self, newx, newy):
        self.world.moveThing(self.xpos, self.ypos, newx, newy)
        self.xpos = newx
        self.ypos = newy
        self.fturtle.goto(self.xpos, self.ypos)


    def tryToMove(self):
        offsetList = [(-1, 1),  (0, 1),  (1, 1),\
                      (-1, 0),           (1, 0),\
                      (-1, -1), (0, -1), (1, -1)]

        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]

        newx = self.xpos + randomOffset[0]
        newy = self.ypos + randomOffset[1]

        while not(0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY()):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            newx = self.xpos + randomOffset[0]
            newy = self.ypos + randomOffset[1]

        if self.world.emptyLocation(newx, newy):
            self.move(newx, newy)


    def tryToBreed(self):
        offsetList = [(-1, 1),  (0, 1),  (1, 1),\
                      (-1, 0),           (1, 0),\
                      (-1, -1), (0, -1), (1, -1)]

        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]

        newx = self.xpos + randomOffset[0]
        newy = self.ypos + randomOffset[1]

        while not(0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY()):
            randomOffsetIndex = random.randrange(len(offsetList))
            randomOffset = offsetList[randomOffsetIndex]
            newx = self.xpos + randomOffset[0]
            newy = self.ypos + randomOffset[1]

        if self.world.emptyLocation(newx, newy):
            child = Fish()
            self.world.addThing(child, newx, newy)
            self.breedTick = 0


    def liveALittle(self):
        offsetList = [(-1, 1),  (0, 1),  (1, 1),\
                      (-1, 0),           (1, 0),\
                      (-1, -1), (0, -1), (1, -1)]

        adjfish = 0
        for offset in offsetList:
            newx = self.xpos + offset[0]
            newy = self.ypos + offset[1]
            if 0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY(): #inbounds
                if (not self.world.emptyLocation(newx, newy)) and isinstance(self.world.lookAtLocation(newx, newy), Fish):
                    #previous check is so that if the location is taken by a fish, then we know we can increment the adjfish counter
                    adjfish += 1

        # Fish dies if two or more fish are adjacent to it
        if adjfish >= 2:
            self.world.delThing(self)
        else:  #if Fish instance did not die
            self.breedTick += 1
            if self.breedTick >= 12:
                self.tryToBreed()

            #self.tryToEat()

            self.tryToMove()











