import random
import turtle
from Berry import Berry
from Fish import Fish


class Bear(object):
    def __init__(self):
        self.bturtle = turtle.Turtle()
        self.bturtle.up()
        self.bturtle.hideturtle()
        self.bturtle.shape("Bear.gif")  # will only work if the file name has been registered in the World class

        self.xpos = 0
        self.ypos = 0
        self.world = None

        self.breedTick = 0
        self.starveTick = 0  # extra attribute for Bears.  we will use to determine if a Bear dies

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
        self.bturtle.goto(self.xpos, self.ypos)
        self.bturtle.showturtle()

    def hide(self):
        self.bturtle.hideturtle()

    def move(self, newx, newy):
        self.world.moveThing(self.xpos, self.ypos, newx, newy)
        self.xpos = newx
        self.ypos = newy
        self.bturtle.goto(self.xpos, self.ypos)


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
            child = Bear()
            self.world.addThing(child, newx, newy)
            self.breedTick = 0

    def tryToEat(self):
        offsetList = [(-1, 1),  (0, 1),  (1, 1),\
                      (-1, 0),           (1, 0),\
                      (-1, -1), (0, -1), (1, -1)]

        adjprey = []
        for offset in offsetList:
            newx = self.xpos + offset[0]
            newy = self.ypos + offset[1]
            if 0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY(): #inbounds
                if (not self.world.emptyLocation(newx, newy)):
                    if isinstance(self.world.lookAtLocation(newx, newy), Fish) or isinstance(self.world.lookAtLocation(newx, newy), Berry) :
                        adjprey.append(self.world.lookAtLocation(newx, newy))

        if len(adjprey) > 0: # there is at least one thing for the Bear to eat
            randomprey = random.choice(adjprey)
            preyx = randomprey.getX()
            preyy = randomprey.getY()

            #Bacause the Bear ate the thing, it must be removed from the world
            self.world.delThing(randomprey)
            self.move(preyx, preyy)
            self.starveTick = 0
        else:
            self.starveTick += 1


    def liveALittle(self):
        #Breed
        self.breedTick += 1
        if self.breedTick >= 8:
            self.tryToBreed()

        #Eat
        self.tryToEat()

        #Die
        if self.starveTick == 10:
            self.world.delThing(self)
        else: #Move
            self.tryToMove()


















