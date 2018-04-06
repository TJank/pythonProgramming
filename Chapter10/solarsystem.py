from sun import *
from planet import *
import turtle

class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0, -height/2.0, width/2.0, height/2.0)

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def addSun(self, asun):
        self.thesun = asun

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

    def freeze(self):
        self.ssscreen.exitonclick()

    def numPlanets(self):
        return len(self.planets)

    def totalMass(self):
        totalmass = self.thesun.getMass()
        for i in range(len(self.planets)):
            totalmass += self.planets[i].getMass()
        return totalmass

    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()
            r = math.sqrt(rx**2 + ry**2)

            accx = G * self.thesun.getMass()*rx/r**3
            accy = G * self.thesun.getMass()*ry/r**3

            p.setXVel(p.getXVel() + dt * accx)
            p.setYVel(p.getYVel() + dt * accy)

