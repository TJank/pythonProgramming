import turtle
import random
from World import World
from Fish import Fish
from Bear import Bear


worldWidth = 50
worldHeight = 25
numberOfFishes = 100
numberOfBears = 5

myWorld = World(worldWidth, worldHeight)
myWorld.draw()
#print(myWorld.grid)


#Randomly position all fishes in the grid
for i in range(numberOfFishes):
    newFish = Fish()  #creates an instance of a Fish
    x = random.randrange(myWorld.getMaxX())
    y = random.randrange(myWorld.getMaxY())
    while not myWorld.emptyLocation(x, y):
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())

    #We found an empty spot so add the Fish
    myWorld.addThing(newFish, x, y)

#Randomly position all fishes in the grid
for i in range(numberOfBears):
    newBear = Bear()  #creates an instance of a Bear
    x = random.randrange(myWorld.getMaxX())
    y = random.randrange(myWorld.getMaxY())
    while not myWorld.emptyLocation(x, y):
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())

    #We found an empty spot so add the Fish
    myWorld.addThing(newBear, x, y)

print(myWorld.getThings())

#Run the simulation -- Equivalent to a Game Engine
#while True:
#    myWorld.liveALittle()

for i in range(1000):
    myWorld.liveALittle()

myWorld.freezeWorld()