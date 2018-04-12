import turtle

class Sun(object):
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.resizemode("user")
        self.sturtle.shapesize(2.5)
        self.sturtle.color("yellow")

    # Accessor methods - Getters
    def getMass(self):
        return self.mass

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y



a_sun = Sun("Bob", 1.4)

# Works because everything in Python is Public
print(a_sun.mass)

# Proper way to retrieve the mass, the method protects the variable
# so you know you are not changin/modifying the variable
print(a_sun.getMass())
