from ch12_book_exercises import *

# myCanvas = Canvas(800, 600)
# myLine = Line(Point(-100,-100), Point(100,100))
# myLine.setColor("blue")
# myLine.setWidth(2)
# myCanvas.draw(myLine)
#
# myCanvas.freeze()


# print(Line.__bases__, Line.__dict__.keys())
# print(myLine)
# print(myCanvas)
# print(myLine.getColor(), myLine.getWidth())
# print(myLine.getP1(), myLine.getP2())
# p = myLine.getP1()
# print(p.getX(), p.getY(), p.getColor())

def test2():
    myCanvas = Canvas(500,500)
    myLine = Line(Point(-100,-100), Point(100,100))
    otherLine = Line(Point(-100, 100), Point(100,-100))
    myLine.setWidth(4)
    myLine.setColor('red')
    myCanvas.draw(myLine)
    myCanvas.draw(otherLine)
    myCanvas.freeze()

test2()



