import turtle

class Berry(object):
    def __init__(self):
        self.bturtle = turtle.Turtle()
        self.bturtle.up()
        self.bturtle.hideturtle()

        self.xpos = 0
        self.ypos = 0
        self.world = None

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

    def liveALittle(self):
        self.bturtle.color('purple')
