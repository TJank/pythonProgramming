import turtle
from numpy import linspace
from scipy import pi, sin, cos

class Canvas(object):
    def __init__(self, w, h, title="Title", bgcolor="yellow"):
        self.width = w
        self.height = h
        self.Objects = []
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=self.width, height=self.height)
        self.screenTitle = title
        self.screen.title(self.screenTitle)
        self.backgroundColor = bgcolor
        self.screen.bgcolor(self.backgroundColor)
        self.turtle.hideturtle()

    def addShape(self, shape):
        self.Objects.append(shape)

    def draw(self, gObject):
        #Add to Canvas
        self.addShape(gObject)

        #Tell gObject which Canvas it belongs to
        gObject.addToCanvas(self)  #gObject is of GeometricObject type
                                   #we will need to code an addToCanvas() method

        #Paint the gObject
        self.turtle.up()
        self.screen.tracer(0)
        gObject._draw(self.turtle) #use the Canvas' turtle to draw the objects
                                   #we will need to code a _draw() method
        self.screen.tracer(1)

    def redraw(self):
        #self.screen.clear()
        self.screen.clearscreen()
        self.turtle.reset()
        self.screen.bgcolor(self.backgroundColor)
        self.screen.title(self.screenTitle)
        self.screen.tracer(0)
        for shape in self.Objects:
            self.turtle.up()
            shape._draw(self.turtle)
        self.screen.tracer(1)
        self.turtle.hideturtle()

    def freeze(self):
        self.screen.exitonclick()
        #turtle.done()

class GeometricObject(object):
    def __init__(self, color, width):
        self.Color = color     #stands for the line-color
        self.Width = width     #stands for the line-thickness
        self.myCanvas = None

    def setColor(self, color):
        self.Color = color
        self.myCanvas.redraw()

    def setWidth(self, width):
        self.Width = width
        self.myCanvas.redraw()

    def getColor(self):
        return self.Color

    def getWidth(self):
        return self.Width

    def addToCanvas(self, aCanvas):
        self.myCanvas = aCanvas

    #An abstract method in Python
    #This method will need to be re-implemented in each object that inherits from
    #GeometricObject
    def _draw(self):
        raise NotImplementedError

class Point(GeometricObject):
    #When initilizing an Object that inherits from another Object
    #You must initialize ALL THE ATTRIBUTES OF THE PARENT Object
    def __init__(self, x, y, color='black', width=1):
        #This is how we tie the init of the child to the init of the parent
        #This method calls the init of the parent
        super().__init__(color, width)

        #Now we define the attributes of this Object, specifically of Point
        self.X = x
        self.Y = y

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getCoord(self):
        return self.X, self.Y

    #We have to implement all abstract classes that exist in the parent class
    #We do this by overriding the implementation of the same method in the parent class
    def _draw(self, aturtle):
        aturtle.up()
        aturtle.goto(self.getX(), self.getY())
        aturtle.down()
        aturtle.dot(self.Width, self.Color)

class Line(GeometricObject):
    def __init__(self, p1, p2, color='black', width=1):
        super().__init__(color, width)
        self.P1 = p1
        self.P2 = p2

    def getP1(self):
        return self.P1

    def getP2(self):
        return self.P2

    def _draw(self, aturtle):
        aturtle.up()
        aturtle.color(self.getColor())
        aturtle.width(self.getWidth())
        aturtle.goto(self.P1.getCoord())   #the interpreter will parse P1 as a Point object
        aturtle.down()
        aturtle.goto(self.P2.getCoord())

class Shape(GeometricObject):
    #A CLOSED SHAPE
    def __init__(self, linecolor='black', linewidth=1, fillcolor=None):
        super().__init__(linecolor, linewidth)
        self.fillColor = fillcolor

    def setFill(self, acolor):
        self.fillColor = acolor
        self.myCanvas.redraw()


#ELLIPSES
#HELPER FUNCITION TO DRAW ELLIPSE
def ellipse(centerPoint, xradius, yradius, ang=pi, Nb=100):
    '''ra - major axis length
      rb - minor axis length
      ang - angle
      x0,y0 - position of centre of ellipse
      Nb - No. of points that make an ellipse

      based on matlab code ellipse.m  written by D.G. Long,
      Brigham Young University, based on the
      CIRCLES.m original
      written by Peter Blattner, Institute of Microtechnology,
      University of
      Neuchatel, Switzerland, blattner@imt.unine.ch
    '''
    if xradius >= yradius:
        ra = max(xradius * 2, yradius * 2)
        rb = min(xradius * 2, yradius * 2)
    else:
        ra = min(xradius * 2, yradius * 2)
        rb = max(xradius * 2, yradius * 2)
    x0 = centerPoint.X
    y0 = centerPoint.Y

    xpos, ypos = x0, y0
    radm, radn = ra, rb
    an = ang

    co, si = cos(an), sin(an)
    the = linspace(0, 2 * pi, Nb)
    X = radm * cos(the) * co - si * radn * sin(the) + xpos
    Y = radm * cos(the) * si + co * radn * sin(the) + ypos
    return X, Y

class Ellipse(Shape):
    def __init__(self, centerPoint, xradius, yradius, linecolor='black', linewidth='1',fillcolor=None):
        super().__init__(linecolor, linewidth, fillcolor)
        self.xRadius = xradius
        self.yRadius = yradius
        self.Center = centerPoint

    def getXRadius(self):
        return self.xRadius

    def getYRadius(self):
        return self.yRadius

    def getCenter(self):
        return self.Center

    #assuming we have a function called ellipse that gives us points along the boundary of an ellipse
    #assuming the output to this function are two lists, one for the X coordinates and one for the Y coordinates
    #then a point in the boundary would look like X[i], Y[i] for some i.

    def _draw(self, aturtle):
        aturtle.color(self.getColor())   #line color
        aturtle.width(self.getWidth())   #line width

        #To DRAW ELLIPSE:
        #ellipse equation is (x-h)**2/a**2 + (y-k)**2/b**2 <= r**2
        #where (h,k) is the centerPoint
        #where a and b are the xRadius and yRadius respectively
        #we use a helper function to generate two lists X and Y of coordinates to paint the boundary of the ellipse

        X, Y = ellipse(self.getCenter(), self.getXRadius(), self.getYRadius())

        if self.fillColor: #fillColor is of None type by default.  It is interpreted as False unless a color is given
            aturtle.fillcolor(self.fillColor)
            aturtle.begin_fill()

        aturtle.goto(X[0], Y[0])
        aturtle.down()
        for i in range(1, len(X)):
            aturtle.goto(X[i], Y[i])

        if self.fillColor:
            aturtle.end_fill()

class Circle(Ellipse):
    def __init__(self, centerPoint, radius, linecolor='black', linewidth=1, fillcolor=None):
        super().__init__(centerPoint, radius, radius, linecolor, linewidth, fillcolor)
        self.Radius = radius

    def getRadius(self):
        return self.Radius


#POLYGONS
class Polygon(Shape):
    #Closed Shapes with corners
    #Polygons that are convex
    def __init__(self, plist, linecolor='black', linewidth='1', fillcolor=None):
        super().__init__(linecolor, linewidth, fillcolor)   #the init of Shape
        self.corners = plist   #a list of Points that define the Polygon.
                               #the list MUST be in the correct order.

    def _draw(self, aturtle):
        aturtle.color(self.getColor())
        aturtle.width(self.getWidth())

        if self.fillColor:
            aturtle.fillcolor(self.fillColor)
            aturtle.begin_fill()

        aturtle.goto(self.corners[0].getCoord())   #corners is a list of Point objects which have a getCoord() method
        aturtle.down()

        for idx in range(1, len(self.corners)):
            aturtle.goto(self.corners[idx].getCoord())

        aturtle.goto(self.corners[0].getCoord())
        if self.fillColor:
            aturtle.end_fill()

class Triangle(Polygon):
    def __init__(self, point1, point2, point3, linecolor='black', linewidth='1', fillcolor=None):
        super().__init__([point1, point2, point3], linecolor, linewidth, fillcolor)
        self.Point1 = point1
        self.Point2 = point2
        self.Point3 = point3

    def getPoint1(self):
        return self.Point1

    def getPoint2(self):
        return self.Point2

    def getPoint3(self):
        return self.Point3

class Rectangle(Polygon):
    def __init__(self, llcorner, urcorner, linecolor='black', linewidth='1', fillcolor=None):
        super().__init__([llcorner, Point(llcorner.getX(), urcorner.getY()), \
                          urcorner, Point(urcorner.getX(), llcorner.getY())], linecolor, linewidth, fillcolor)

        self.LLcorner = llcorner
        self.URcorner = urcorner

    def getLLcorner(self):
        return self.LLcorner

    def getURcorner(self):
        return self.URcorner

# class Rectangle(Polygon):
#     def __init__(self, ulcorner, width, height, linecolor='black', linewidth='1', fillcolor=None):
#         super().__init__([ulcorner, Point(ulcorner.getX() + width, ulcorner.getY()), \
#                           Point(ulcorner.getX() + width, ulcorner.getY() - height), \
#                           Point(ulcorner.getX(), ulcorner.getY() - height)], linecolor, linewidth, fillcolor)
#         self.corner = ulcorner
#         self.width = width
#         self.height = height



class Square(Rectangle):
    def __init__(self, llcorner, sideLength, linecolor='black', linewidth='1', fillcolor=None):
        super().__init__(llcorner, Point(llcorner.getX() + sideLength, llcorner.getY() + sideLength),\
                         linecolor, linewidth, fillcolor)
        self.SideLength = sideLength

    def getSideLength(self):
        return self.SideLength


if __name__ == "__main__"
    ###############################################
    ###############################################
    #Create a Canvas
    #aCanvas = Canvas(1200, 700)

    #Draw some Points
    # p1 = Point(1, 1, color='#E81F3F', width=4)
    # p2 = Point(-15, 100, color='#42E8F3', width=2)
    # # aCanvas.draw(p1)
    # # aCanvas.draw(p2)
    #
    #
    # #Draw a Line
    # line1 = Line(p1, p2)
    # line2 = Line(Point(100, 200), Point(200, -100), color='blue', width=3)
    # aCanvas.draw(line1)
    # aCanvas.draw(line2)

    #making a change to an existing line
    #aCanvas.turtle._delay(5000)
    #line2.setColor('yellow')

    #aCanvas.turtle._delay(5000)
    #line2.setWidth(5)

    #
    # #Draw an Ellipse
    # ellipse1 = Ellipse(Point(0,0),20.5, 50, fillcolor="red")
    # aCanvas.draw(ellipse1)
    #
    #
    # ellipse2 = Ellipse(Point(-100, 100), 40, 100, linecolor='blue', linewidth=5, fillcolor='yellow')
    # #aCanvas.draw(ellipse2)
    #
    # #ellipse3 = Ellipse(Point(0,0), 50, 50, linecolor='green', linewidth=2, fillcolor='black')
    # #aCanvas.draw(ellipse3)
    #
    # circle1 = Circle(Point(0, 0), 100, linecolor='green', fillcolor="green")
    # aCanvas.draw(circle1)


    # #Draw a Polygon: Non-convex
    #pointList = [Point(0, 0), Point(24.3, -70), Point(0, 50), Point(-20.5, 50), Point(-100, 30)]
    # p1 = Point(10,15)
    # p2 = Point(30,15)
    # p3 = Point(30,0)
    # p4 = Point(10,0)
    # pointList = [p1,p4,p2,p3]
    # polygon1 = Polygon(pointList, fillcolor="#42E8F3", linewidth=2)
    # aCanvas.draw(polygon1)



    # #Draw a Triangle
    # triangle1 = Triangle(Point(-70, 90), Point(0, 200), Point(30, 40), linecolor='green', fillcolor='blue')
    # aCanvas.draw(triangle1)
    #
    # #Draw a Rectangle
    # rectangle1 = Rectangle(Point(12, 17), Point(220, 45), fillcolor='magenta')
    # rectangle1 = Rectangle(Point(12,17), 100, 300, fillcolor="red", linecolor="blue", linewidth="3")
    # aCanvas.draw(rectangle1)
    #
    # #Draw a Square
    # square1 = Square(Point(0, 10), 100, fillcolor='red')
    # aCanvas.draw(square1)
    #
    # #Exercise:
    # #Draw a house
    # def drawHouse():
    #     # To complete this example will require creation of Rectangle and Circle
    #     myCanvas = Canvas(800, 600)
    #     house = Rectangle(Point(-100, -100), Point(100, 100), fillcolor='blue')
    #     door = Rectangle(Point( 50, -100), Point(0, 0), fillcolor='white')
    #     #roof1 = Line(Point(-100, 100), Point(0, 200), width=3)
    #     #roof2 = Line(Point(0, 200), Point(100, 100), width=3)
    #
    #     roof = Triangle(Point(-100, 100), Point(0, 200), Point(100, 100), linewidth=3, fillcolor='brown')
    #     myCanvas.draw(house)
    #     myCanvas.draw(door)
    #     #myCanvas.draw(roof1)
    #     #myCanvas.draw(roof2)
    #     myCanvas.draw(roof)
    #     sun = Circle(Point(150, 250), 20, fillcolor='yellow')
    #     myCanvas.draw(sun)
    #
    #     myCanvas.freeze()
    #
    # drawHouse()
    # #
    # #
    # # ###############################################
    # aCanvas.freeze()




