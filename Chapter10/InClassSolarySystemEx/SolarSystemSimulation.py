from SolarSystem import SolarSystem
from Sun import Sun
from Planet import Planet


def createAndAnimate():
    ss = SolarSystem(2, 2)

    sun = Sun("SUN", 10)
    ss.addSun(sun)

    m = Planet("Mercury", 1000, 0.2, 1, 0, 2, "orange")
    ss.addPlanet(m)

    e = Planet("Earth", 5000, 0.3, 1.3, 0, 2, "blue")
    ss.addPlanet(e)

    ma = Planet("Mars", 9000, 0.5, 1.2, 0, 1.63, "red")
    ss.addPlanet(ma)

    p = Planet("Pluto", 500, 0.9, .5, 0, .5, "gray")
    ss.addPlanet(p)

    # a = Planet("Asteroid", 500, 1.0, 0, .75, "cyan")
    # ss.addPlanet(a)

    numCycles = 10000
    for i in range(numCycles):
        ss.movePlanets()

    # while True:
    #     ss.movePlanets()
    #     # You can add functionality to break away from the loop given some condition
    #     # use the keyword break
    #     break


    ss.freeze()

createAndAnimate()