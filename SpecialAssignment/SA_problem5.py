from turtle import Turtle, mainloop
import random
import math

# Modify the spaceinvaders game so that the LaserCanon() object moves sideways using the arrow keys
# for left and right, without going past the screen boundaries. Prevent the LaserCanon() object from
# changing direction. It should only fire a Bomb in a straight vertical direction. Use the up arrow key
# rathen than the “s” key to fire a bomb. This modification changes the game dynamic so that it mimic
# space invaders more accurately


class LaserCannon(Turtle):
    def __init__(self, xmin, xmax, ymin, ymax):
        super().__init__()
        self.screen = self.getscreen()
        self.screen.bgcolor("light green")
        self.screen.setworldcoordinates(xmin, ymin, xmax, ymax)
        self.screen.onkey(self.aimLeft, "Left")#we need to create a method for aim
        self.screen.onkey(self.aimRight, "Right")
        self.screen.onkey(self.shoot, "Up")   #we need to create a method for shoot
        self.screen.onkey(self.quit, "q")    #we need to create a method for quit


    def aimLeft(self):
        #print(self.heading())
        if self.heading() >= 180:
            return "Can't aim backwards"
        else:
            self.left(10)

    def aimRight(self):
        #print(self.heading())
        if self.heading() == 0:
            return "Can't aim backwards"
        else:
            self.right(10)

    def shoot(self):
        Bomb(self.heading(), 5)    #we do not know at this point what this does, but we know we are creating a Bomb object
                                   #first argument is the direction, the second argument is the speed

    def quit(self):
        self.screen.bye()


class BoundedTurtle(Turtle):  #any object bounded by the screen
    def __init__(self, speed, xmin=-200, xmax=200, ymin=0, ymax=400):  #the bounded turtle object has default values
        super().__init__()
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.speed = speed

    def outOfBounds(self):
        xpos, ypos = self.position()  #tuple indicating the current position of the BoundedTurtle
        out = False                   # assume the BoundedTurtle is inside of the bounds
        if xpos < self.xmin or xpos > self.xmax:
            out = True
        if ypos < self.ymin or ypos > self.ymax:
            out = True
        return out

    def move(self):
        self.forward(self.speed)
        if self.outOfBounds():
            self.remove()            #we need a method to remove the object from the screen
        else:
            self.getscreen().ontimer(self.move, 200)   #this method .ontimer creates a callback to .move in the current instance
                                                       # every 200 seconds
    def remove(self):
        self.hideturtle()


class Bomb(BoundedTurtle):
    def __init__(self, initHeading, speed):
        super().__init__(speed)
        self.initHeading = initHeading
        self.shape("circle")
        self.color('red', 'red')
        self.resizemode('user')
        self.setheading(initHeading)
        self.up()
        self.turtlesize(.25)
        self.getscreen().ontimer(self.move, 100)

    def distance(self, other):  #calculate distance between two BoundedTurtles for collision detection
        p1 = self.position()
        p2 = other.position()
        a = p1[0] - p2[0]
        b = p1[1] - p2[1]
        dist = math.sqrt(a**2 + b**2)
        return dist

    #overriding superclass move
    def move(self):
        exploded = False
        self.forward(self.speed)
        #collision detection
        for i in Alien.getAliens(): # this assumes that Alien in a class that can be iterated and that contains a method
                                    # .getAliens
            if self.distance(i) < 5:# if bomb and alien are within 5 units then the bomb should trigger and explode
                i.remove()          # i is an Alien object, thus Alien should contain a .remove method
                exploded = True

        if self.outOfBounds() or exploded:
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 100)

class Alien(BoundedTurtle):
    alienList = []  #class global variable to hold all objects that we identify as "aliens"

    @staticmethod
    def getAliens():
        return [x for x in Alien.alienList if x.alive]

    def __init__(self, speed, xmin, xmax, ymin, ymax):
        super().__init__(speed, xmin, xmax, ymin, ymax)
        self.getscreen().tracer(0)
        self.up()
        if 'PurpleAlien.gif' not in self.getscreen().getshapes():
            self.getscreen().addshape("PurpleAlien.gif")   #this is needed especially when the game starts
        self.shape('PurpleAlien.gif')
        self.goto(random.randint(xmin+1, xmax-1), ymax-20)
        self.setheading(random.randint(250, 290))
        self.getscreen().tracer(1)
        Alien.alienList = [x for x in Alien.alienList if x.alive]
        Alien.alienList.append(self)
        self.alive = True
        self.getscreen().ontimer(self.move, 200)   #rely on the move method from the superclass

    #override remove method
    def remove(self):
        self.alive = False
        self.hideturtle()


#Game engine
class AlienInvaders:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def play(self):
        self.mainWin = LaserCannon(self.xmin, self.xmax, self.ymin, self.ymax).getscreen()
        self.mainWin.ontimer(self.addAlien, 1000)   # this means we need to code a .addAlien method
        self.mainWin.listen()  #we add this so that all event handlers are running (or threads are running)
        mainloop()

    def addAlien(self):
        if len(Alien.getAliens()) < 7:
            Alien(1, self.xmin, self.xmax, self.ymin, self.ymax)
        self.mainWin.ontimer(self.addAlien, 1000)


game = AlienInvaders(-200, 200, 0, 400)  #matches the default values for the BoundedTurtle object
game.play()      #game engine at work
