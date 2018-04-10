import turtle, math


class SolarSystem(object):
    def __init__(self, width, height):
        self.aSun = None
        self.planets = []

        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2, -height/2, width/2, height/2)
        self.ssscreen.tracer(50)

    # Mutator Method
    def addSun(self, asun):
        self.aSun = asun

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def freeze(self):
        self.ssscreen.exitonclick()

    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

            rx = self.aSun.getXPos() - p.getXPos()
            ry = self.aSun.getYPos() - p.getYPos()
            r = math.sqrt(rx ** 2 + ry ** 2)

            accx = G * self.aSun.getMass() * rx/r**3
            accy = G * self.aSun.getMass() * ry/r**3

            p.setXVel(p.getXVel() + dt * accx)
            p.setYVel(p.getYVel() + dt * accy)




