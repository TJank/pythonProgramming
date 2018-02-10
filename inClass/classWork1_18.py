import graphics
import turtle

hector = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)


#hector.pencolor(0.71, 0.76, 0.228)
hector.pencolor(255, 0, 0)
graphics.draw_square(hector, 100)

graphics.move_turtle(hector, -100, 100)

hector.pencolor(0, 255, 0)
graphics.draw_polygon(hector, 50, 8)

graphics.move_turtle(hector, 200, 200)

# a circle using the draw_polygon()
#graphics.draw_polygon(hector, 1, 360)

hector.pencolor(255, 255, 0)
graphics.draw_circle(hector, 32)




















































































turtle.done()