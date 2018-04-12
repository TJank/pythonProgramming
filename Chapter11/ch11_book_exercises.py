
import turtle
# Creating World class
class World(object):
    def __init__(self, mx, my):
        self.maxX = mx
        self.maxY = my
        self.thingList = []
        self.grid = []

        for arow in range(self.maxY):
            row = []
            for acol in range(self.maxX):
                row.append(None)
            self.grid.append(row)

        self.wturtle = turtle.Turtle()
        self.wscreen = turtle.Screen()
        self.wscreen.setworldcoordinates(0,0,self.maxX-1, self.maxY-1)
        self.wscreen.addshape("Bear.gif")
        self.wscreen.addshape("Fish.gif")
        self.wturtle.hideturtle()

        
