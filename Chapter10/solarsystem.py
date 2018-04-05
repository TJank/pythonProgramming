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