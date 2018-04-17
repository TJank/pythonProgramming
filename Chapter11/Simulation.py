import random

from Bear import Bear
from Fish import Fish
from World import World


####SIMULATION

def mainSimulation():
    numberOfBears = 10
    numberOfFish = 100
    numberOfTurns = 1000
    worldWidth = 50
    worldHeight = 25
    
    myWorld = World(worldWidth, worldHeight)
    myWorld.draw()

    for i in range(numberOfFish):
        newfish = Fish()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
            
        myWorld.addThing(newfish, x, y)
        
    for i in range(numberOfBears):
        newbear = Bear()
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
        while not myWorld.emptyLocation(x, y):
            x = random.randrange(myWorld.getMaxX())
            y = random.randrange(myWorld.getMaxY())
            
        myWorld.addThing(newbear, x, y)
    
    for i in range(numberOfTurns):
        myWorld.liveALittle()

    #while True:
        #myWorld.liveALittle()

    myWorld.freezeWorld()


mainSimulation()




####PRACTICE
# myWorld = World(50, 25)
# 
# print(myWorld.grid)
# 
# myFish = Fish()
# myWorld.addThing(myFish, 10, 10)
# print(myWorld.emptyLocation(10, 10))
# print(myWorld.lookAtLocation(10, 10))
# 
# myWorld.draw()
# 
# myBear = Bear()
# myWorld.addThing(myBear, 20, 20)
# myBear2 = Bear()
# myWorld.addThing(myBear2, 20, 10)
# 
# #myFish.move(20, 20)
# for x in range(200):
#     myFish.tryToMove()
#     myFish.tryToBreed()
#     myBear.tryToMove()
#     myBear.tryToEat()
#     myBear2.tryToMove()
#     myBear2.tryToEat()
# 
# 
# 
# print(myWorld.emptyLocation(10, 10))
# print(myWorld.lookAtLocation(10, 10))
# 
# 
# myWorld.freezeWorld()

