def draw_square(a_turtle, side_length):
    d = 90
    for i in range(4):
        a_turtle.forward(side_length)
        a_turtle.right(d)

def draw_spiral(a_turtle, side_length, offset, steps):
    sl = side_length
    a_turtle.right(180)
    for i in range(steps):
        a_turtle.forward(sl)
        a_turtle.left(90)
        sl = sl + offset

def draw_triangle(a_turtle, side_length):
    for i in range(3):
        a_turtle.forward(side_length)
        a_turtle.left(120)

def draw_polygon(a_turtle, side_length, num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        a_turtle.forward(side_length)
        a_turtle.right(angle)

# Wrapper function, calls draw_polygon
def draw_circle(a_turtle, radius):
    from math import pi
    a_turtle.speed("fastest")
    circumference = 2 * pi * radius
    side_length = circumference/360
    draw_polygon(a_turtle, side_length, 360)

def move_turtle(a_turtle, x, y):
    # move the turtle to new position
    a_turtle.penup()  # stop draw, turtle picks his tail up
    a_turtle.goto(x, y)  # move to new location
    a_turtle.pendown()  # pen down, start drawing





























