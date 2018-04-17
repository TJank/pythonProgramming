import turtle

class Canvas(object):
    def __init__(self, w, h, title="Title", bgcolor="yellow"):
        self.width = w
        self.height = h
        self.objects = []
        self.cturtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=self.width, height=self.height)
        self.screen.title(title)
        self.bgcolor = bgcolor
        self.screen.bgcolor(self.bgcolor)
        self.cturtle.hideturtle()

    def addShape(self, shape):
        self.objects.append(shape)

    def draw(self, gObject):
        # First: add object to canvas
        self.addShape(gObject)

        # Tell gObject which canvas it belongs to and draw it
        gObject.addToCanvas(self)       # a method to be coded for all goemetric object

        self.cturtle.up()
        self.screen.tracer(0)
        gObject._draw(self.cturtle)
        self.screen.tracer(1)
        


