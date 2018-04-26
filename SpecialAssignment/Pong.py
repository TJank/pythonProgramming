from turtle import Turtle
import turtle


class World(object):
    def __init__(self, maxx, maxy):
        self.maxX = maxx
        self.maxY = maxy
        self.wturtle = turtle.Turtle()
        self.wturtle.hideturtle()
        self.wscreen = turtle.Screen()
        self.wscreen.setworldcoordinates(-self.maxX, -self.maxY, self.maxX, self.maxY)
        self.players = []
        self.wscreen.addshape("rectangle1.gif")

    def freeze(self):
        self.wscreen.exitonclick()

    def addPlayer1(self):
        self.players.append(Player1)

    def drawPlayArea(self):
        self.wturtle.penup()
        self.wturtle.goto(0,-300)
        self.wturtle.left(90)
        for i in range(1, 600, 10):
            self.wturtle.pendown()
            self.wturtle.forward(10)
            self.wturtle.penup()
            self.wturtle.forward(10)



class Player1(Turtle):
    def __init__(self):
        super().__init__()
        self.xcord = -280
        self.ycord = -280
        self.shape("rectangle")
        self.color("red")
        self.world = None
        self.score = 0
        self.screen.onkey(self.moveUp, "w")
        self.screen.onkey(self.moveDown, "s")
        self.shape("rectangle1.gif")


    def moveUp(self):
        self.forward(15)

    def moveDown(self):
        self.backward(15)



myworld = World(300,300)
myworld.drawPlayArea()
myworld.addPlayer1()
myworld.freeze()