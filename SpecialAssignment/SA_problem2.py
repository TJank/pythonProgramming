from turtle import Turtle, mainloop

# Modify the Etch class in EtchASketch.py so that the turtle fills with color by pressing on the keyboard
# key “f”. Filling with color requires begin_fill() and end_fill() but make sure that a single callback
# function handles both with the press of the “f” key. Do not worry about the actual color; it will default
# to the current color the turtle has. [Hint: use a self.isFilling flag, set it to false and alternate its value
# upon each press of the “f” key]

class Etch(Turtle):
    def __init__(self):
        super().__init__()   #calls the init of Turtle
        self.screen = self.getscreen()
        self.color('blue')
        self.shape('turtle')
        self.pensize(2)
        self.distance = 5
        self.turn = 10
        self.screen.onkey(self.fwd, "Up")
        self.screen.onkey(self.bkwd, "Down")
        self.screen.onkey(self.leftTurn, "Left")
        self.screen.onkey(self.rightTurn, "Right")
        self.screen.onkey(self.colorRed, "r")
        self.screen.onkey(self.colorBlue, "b")
        self.screen.onkey(self._up, "u")
        self.screen.onkey(self._down, "d")
        self.screen.onkey(self.fill, "f")
        self.isFilling = False
        self.speed("fastest")
        self.screen.listen()
        self.main()

    def fill(self):
        if self.isFilling == False:
            self.isFilling = True
            self.fillcolor("purple")
            self.begin_fill()
            print("WE ARE BEGINNING TO FILL")

        elif self.isFilling == True:
            self.isFilling = False
            self.end_fill()
            print("SHAPE SHOULD BE FILLED")

        else:
            print("UHH OHH SOMETHING WENT WRONG")


    def _up(self):
        self.up()

    def _down(self):
        self.down()

    def colorRed(self):
        self.color("red")

    def colorBlue(self):
        self.color("blue")

    def fwd(self):
        self.forward(self.distance)

    def bkwd(self):
        self.backward(self.distance)

    def leftTurn(self):
        self.left(self.turn)

    def rightTurn(self):
         self.right(self.turn)

    def main(self):
        mainloop()

#A way of running the program with an instance of the object Etch
if __name__ == '__main__':
    etch = Etch()


