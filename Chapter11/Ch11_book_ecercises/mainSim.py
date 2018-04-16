import Bear, Fish
import World
import random

def mainSim():
    numberOfBears = 10
    numberOfFish = 10
    worldLifeTime = 2500
    worldWidth = 50
    worldHeight = 25

    myworld = World(worldWidth, worldHeight)
    myworld.draw()

    for i in range(numberOfFish):
        newfish = Fish()
        x = random.randrange(myworld.getMaxY())
        y = random.randrange(myworld.GetMaxY())
        while not myworld.emptyLocation(x, y):
            x = random.randrange(myworld.getMaxY())
            y = random.randrange(myworld.getMaxY())
        myworld.addThing(newfish, x, y)

    for i in range(numberOfBears):
        newBear = Bear()
        x = random.randrange(myworld.getMaxY())
        y = random.randrange(myworld.GetMaxY())
        while not myworld.emptyLocation(x, y):
            x = random.randrange(myworld.getMaxY())
            y = random.randrange(myworld.getMaxY())
        myworld.addThing(newBear, x, y)

    for i in range(worldLifeTime):
        myworld.liveALittle()

    myworld.freezeworld()
