import turtle

#import turtle
#help(turtle) to get help for turtle commands

helga = turtle.Turtle() # create a turtle for us to command

# Draw a square
#x = 100
#d = 90
#helga.forward(x)
#hgelga.right(d)
#helga.forward(x)
#helga.right(d)
#helga.forward(x)
#helga.right(d)
#helga.forward(x)
#helga.right(d)
#x = 100
#d = 90
#for i in range(4):
    #helga.forward(x)
    #helga.right(d)

#as a function
def draw_square(side_length, a_turtle):
    d = 90
    for i in range(4):
        a_turtle.forward(side_length)
        a_turtle.right(d)

#draw_square(400, helga)

#turtle.done()

# 1-18 class work
def draw_spiral(aTurtle, sideLength, offset, steps):
    sl = sideLength
    aTurtle.right(180)
    for i in range(steps):
        aTurtle.forward(sl)
        aTurtle.left(90)
        sl = sl + offset
#Outward spiral
#draw_spiral(helga, 40, 4, 16)

# Inward spiral
#draw_spiral(helga, 100, -4, 20)

def draw_triangle(aTurtle, sideLength):
    for i in range(3):
        aTurtle.forward(sideLength)
        aTurtle.left(120)


#draw_triangle(helga, 100)

# Draw 12 pointed star!
helga.forward(50)
helga.right(165)
helga.forward(50)
helga.right(165)
helga.forward(50)
helga.right(165)
helga.forward(50)
helga.right(165)
helga.forward(50)
helga.right(165)
helga.forward(50)
helga.right(165)
helga.forward(50)
helga.right(165)
helga.forward(50)
helga.right(165)
helga.forward(50)
helga.right(165)
helga.forward(50)
helga.right(165)


def star(turtle, n, d):
    for i in range(n):
        angle = 180.0 - 180.0 / n
        turtle.forward(d)
        turtle.right(angle)
        turtle.forward(d)

#star(helga, 12, 100)


turtle.done()