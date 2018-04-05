from sun import *
from planet import *
from solarsystem import *

ss = SolarSystem(2,2)

sun = Sun("Sun", 5000,10, 5800)
ss.addSun(sun)

m = Planet("Mercury", 19.5,1000,.25,"purple")
ss.addPlanet(m)

m = Planet("Earth", 47.5,5000,0.3,"blue")
ss.addPlanet(m)

m = Planet("Mars", 50,9000,0.5, "red")
ss.addPlanet(m)

m = Planet("Jupiter", 100,49000,0.7,"green")
ss.addPlanet(m)

ss.freeze()

