
from turtle import Turtle, mainloop
#Modify the Etch class in EtchASketch.py so that the turtle changes direction towards the position
#where you click with the mouse pointer.


class Etch(Turtle):
    def __init__(self):
        super().__init__()   #calls the init of Turtle
        self.screen = self.getscreen()
        self.color('blue')
        self.shape('turtle')
        self.pensize(2)
        self.screen.onclick(self.goThisWay)
        self.screen.onkey(self.colorRed, "r")
        self.screen.onkey(self.colorBlue, "b")
        self.screen.onkey(self._up, "u")
        self.screen.onkey(self._down, "d")
        self.speed("fastest")
        self.screen.listen()
        self.main()

    def goThisWay(self, x, y):
        heading = self.towards(x, y)
        self.setheading(heading)
        self.forward(50)

    def _up(self):
        self.up()

    def _down(self):
        self.down()

    def colorRed(self):
        self.color("red")

    def colorBlue(self):
        self.color("blue")

    def main(self):
        mainloop()

#A way of running the program with an instance of the object Etch
if __name__ == '__main__':
    etch = Etch()


