import turtle, random

class World(object):
    def __init__(self, maxx, maxy):
        self.maxX = maxx
        self.maxY = maxy
        self.thingList = []
        self.grid = []

        #To initilize the world to None (empty) objects at each position
        for arow in range(self.maxY):
            row = []
            for acol in range(self.maxX):
                row.append(None)
            self.grid.append(row)

        self.wturtle = turtle.Turtle()
        self.wscreen = turtle.Screen()
        self.wscreen.setworldcoordinates(0, 0, self.maxX - 1, self.maxY - 1)

        #Only registered shapes can be used by issuing the command shape(shapename)
        self.wscreen.addshape("Bear.gif")
        self.wscreen.addshape("Fish.gif")
        self.wturtle.hideturtle()  #so we don't see the arrow

    #Paint the grid
    def draw(self):
        self.wscreen.tracer(0)  #fast painting
        self.wturtle.forward(self.maxX - 1)
        self.wturtle.left(90)
        self.wturtle.forward(self.maxY - 1)
        self.wturtle.left(90)
        self.wturtle.forward(self.maxX - 1)
        self.wturtle.left(90)
        self.wturtle.forward(self.maxY - 1)
        self.wturtle.left(90)
        for i in range(self.maxY - 1):
            self.wturtle.forward(self.maxX - 1)
            self.wturtle.backward(self.maxX - 1)
            self.wturtle.left(90)
            self.wturtle.forward(1)
            self.wturtle.right(90)
        self.wturtle.forward(1)
        self.wturtle.right(90)
        for i in range(self.maxX - 1):
            self.wturtle.forward(self.maxY - 1)
            self.wturtle.backward(self.maxY - 1)
            self.wturtle.left(90)
            self.wturtle.forward(1)
            self.wturtle.right(90)
        self.wscreen.tracer(1)


    def freezeWorld(self):
        self.wscreen.exitonclick()

    def getMaxX(self):
        return self.maxX

    def getMaxY(self):
        return self.maxY

    def addThing(self, athing, x, y):
        athing.setX(x)  #eventually we will define an object (thing) that will have a .setX() method
        athing.setY(y)

        self.grid[y][x] = athing
        athing.setWorld(self)  #this says that the object (thing) will be assigned to this instance of the world

        self.thingList.append(athing)
        athing.appear()

    def delThing(self, athing):
        athing.hide()
        self.grid[athing.getY()][athing.getX()] = None
        self.thingList.remove(athing)

    def moveThing(self, oldx, oldy, newx, newy):
        self.grid[newy][newx] = self.grid[oldy][oldx]
        self.grid[oldy][oldx] = None

    def liveALittle(self):
        if self.thingList != []:
            athing = random.randrange(len(self.thingList))
            randomthing = self.thingList[athing]
            randomthing.liveALittle()  #calling the method of the object (thing)

    def emptyLocation(self, x, y):
        if self.grid[y][x] == None:
            return True
        else:
            return False

    def lookAtLocation(self, x, y):
        return self.grid[y][x]






