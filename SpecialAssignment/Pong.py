from turtle import Turtle
import turtle
import random


class World(object):
    def __init__(self, maxx, maxy):
        self.maxX = maxx
        self.maxY = maxy
        self.wturtle = turtle.Turtle()
        self.wturtle.hideturtle()
        self.wscreen = turtle.Screen()
        self.wscreen.setworldcoordinates(-self.maxX, -self.maxY, self.maxX, self.maxY)
        self.players = []
        self.wscreen.addshape("bumper.gif")

    def freeze(self):
        self.wscreen.exitonclick()

    def addPlayer1(self, aplayer):
        self.players.append(aplayer)

    def drawPlayArea(self):
        self.wturtle.hideturtle()
        self.wturtle.penup()
        self.wturtle.goto(0,-300)
        self.wturtle.left(90)
        for i in range(1, 600, 10):
            self.wturtle.pendown()
            self.wturtle.forward(10)
            self.wturtle.penup()
            self.wturtle.forward(10)

    def placePlayer(self, aplayer):
        aplayer.goto(aplayer.xcord, aplayer.ycord)
        aplayer.showturtle()

    def addBall(self, aball):
        aball.goto(aball.xcord, aball.ycord)


    def play(self):
        self.wscreen.mainloop()


class Player1(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.xcord = -280
        self.ycord = -280
        self.shape("square")
        self.color("red")
        self.world = None
        self.score = 0
        self.screen = self.getscreen()
        self.screen.onkey(self.moveUp, "w")
        self.screen.onkey(self.moveDown, "s")
        self.shape("bumper.gif")

    def setWorld(self, aworld):
        self.world = aworld

    def moveUp(self):
        self.forward(15)

    def moveDown(self):
        self.backward(15)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.speed(1)
        #self.setposition(0, random.randint(-100, 100))
        self.xcord = 0
        self.ycord = 0
        self.right(random.randint(0, 360))
        self.world = None

    def setWorld(self, aworld):
        self.world = aworld



myworld = World(400,400)
myworld.drawPlayArea()


firstplayer = Player1()
myworld.addPlayer1(firstplayer)
firstplayer.setWorld(myworld)
myworld.placePlayer(firstplayer)

pongball = Ball()
pongball.setWorld(myworld)
myworld.addBall(pongball)

myworld.play()
