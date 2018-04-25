from threading import Thread
import time
import turtle

# Listing 13.1 PG 425
class EventHandler(Thread):
    def __init__(self):
        super().__init__()
        self.queue = []
        self.eventKeeper = {}

    def addEvent(self, eventName):
        self.queue.append(eventName)

    def registerCallback(self, event, func):
        self.eventKeeper[event] = func

    def run(self):
        while (True):
            if len(self.queue) > 0:
                nextEvent = self.queue.pop(0)
                callback = self.eventKeeper[nextEvent]
                callback()
            else:
                time.sleep(1)


# SESSION 13.1
def myMouse():
    print('Oh no the mouse was clicked.')
#
def myKey():
    print('A key has been pressed.')
#
# eh = EventHandler()
# eh.registerCallback('key', myKey())
# eh.registerCallback('mouse', myMouse())
# eh.addEvent('mouse')
# eh.addEvent('key')
# eh.addEvent('mouse')

# SESSION 13.2
# eh = EventHandler()
# eh.addEvent('mouse')
# eh.addEvent('key')
# eh.addEvent('mouse')
# eh.registerCallback('key', myKey)
# eh.registerCallback('mouse', myMouse)
# eh.start()

class Etch(object):
    def __init__(self):
        self.myT = turtle.Turtle()
        self.mySCreen = turtle.Screen()
        self.myT.color('blue')
        self.myT.pensize(2)
        self.myT.speed(0)
        self.distance = 5
        self.turn = 10
        self.mySCreen.onkey(self.fwd, 'Up')
        self.mySCreen.onkey(self.bkwd, 'Down')
        self.mySCreen.onkey(self.left, 'Left')
        self.mySCreen.onkey(self.right, 'Right')
        self.mySCreen.onkey(self.quit, 'q')
        self.mySCreen.listen()

    def fwd(self):
        self.myT.forward(self.distance)

    def bkwd(self):
        self.myT.backward(self.distance)

    def left(self):
        self.myT.left(self.turn)

    def right(self):
        self.myT.right(self.turn)

    def quit(self):
        self.mySCreen.bye()

    def main(self):
        turtle.mainloop()

from turtle import Turtle
class ETCH(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = self.getscreen()
        self.color = 'blue'
        self.pensize(2)
        self.speed(0)
        self.distance = 5
        self.turn = 10
        self.screen.onkey(self.fwd, 'Up')
        self.screen.onkey(self.bkwd, 'Down')
        self.screen.onkey(self.left, 'Left')
        self.screen.onkey(self.right, 'Right')
        self.screen.onkey(self.quit, 'q')
        self.screen.listen()
        self.main()

    def fwd(self):
        self.forward(self.distance)

    def bkwd(self):
        self.backward(self.distance)

    def left5(self):
        self.left(self.turn)

    def right5(self):
        self.right(self.turn)

    def quit(self):
        self.screen.bye()

    def main(self):
        mainloop()

draw = Etch()
draw.main()



