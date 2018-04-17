from ch12_book_exercises import *

myCanvas = Canvas(800, 600)
myLine = Line(Point(-100,-100), Point(100,100))
myCanvas.draw(myLine)

myCanvas.freeze()