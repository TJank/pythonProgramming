from sun import *
from planet import *
from solarsystem import *

def creatSSandAnimate():
    ss = SolarSystem(2,2)

    sun = Sun("SUN", 5000,10,5800)
    ss.addSun(sun)

    m = Planet("MERCURY", 19.5,1000,.25,0,2,"purple")
    ss.addPlanet(m)

    m = Planet("EARTH", 47.5,5000,0.3,0,2.0, "blue")
    ss.addPlanet(m)

    m = Planet("MARS", 50, 9000, .5, 0, 1.63, "red")
    ss.addPlanet(m)

    m = Planet("JUPITER", 100, 49000, 0.7, 0, 1, "green")
    ss.addPlanet(m)

    numTimePeriods = 2000
    for amove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

creatSSandAnimate()

