import math

# INT methods pg 332
# count = 1
# count = count.__add__(1)
# print(count)
#
# mylist = [1,2,3,4,5,6,7,8,9]
# print(mylist.__getitem__(1))

# Listing 10.1 Planet class with a constructor
class Planet:
    def __init__(self, iname, irad, im, idist, moons):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.numMoons = moons
        self.moonList = []

    # Listing 10.2 Acessor Methods pg 336
    def getName(self):
        return self.name
    def getRadius(self):
        return self.radius
    def getMass(self):
        return self.mass
    def getDistance(self):
        return self.distance

    def getMoons(self):
        return self.numMoons

    # Listing 10.3 pg 337
    def getCircumference(self):
        c = 2 * math.pi * self.radius
        return c

    def getVolume(self):
        v = 4/3 * math.pi * self.radius**3
        return v

    def getSurfaceArea(self):
        sa = 4 * math.pi * self.radius**2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def show(self):
        print(self.name)

    def __str__(self):
        return self.name

    # MUTATOR Methods
    def setName(self, newname):
        self.name = newname

    def setMoons(self, num_new_moons):
        self.numMoons = self.numMoons + num_new_moons

    def addMoon(self, moon_name):
        self.moonList.append(moon_name)







myplanet = Planet("X25", 45, 198, 1000,3)
# print(myplanet)
# print(myplanet.getName(), myplanet.getMass(),myplanet.name)
# print(myplanet.getVolume(), myplanet.getSurfaceArea(), myplanet.getDensity())
#myplanet.setName("Gamma Hydra")
myhome = Planet("Earth", 6371, 5.97e24,152097701,1)
myhome.show()
print(myhome.__str__())
print(myhome)
print(str(myhome))

# Listing 10.7 pg 348
class Sun:
    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp

    def getMass(self):
        return self.mass

    def __str__(self):
        return self.name

    def getTemperature(self):
        return self.temp

    def getVolume(self):
        v = 4/3 * math.pi * self.radius**3
        return v

    def getSurfaceArea(self):
        sa = 4 * math.pi * self.radius**2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def setName(self, newname):
        self.name = newname

    def getRadius(self):
        return self.radius


# Listing 10.8 pg 349
class SolarSystem:
    def __init__(self, asun):
        self.thesun = asun
        self.planets = []

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)



# DO EXERCISES PG 343
# 10.13-10.26

class sentence:
    def __init__(self, a_string):
        self.sentence = a_string


    # Methods
    def getSentence(self):
        return self.sentence

    def getWords(self):
        sentList = self.sentence.split(' ')
        return sentList

    def getLength(self):
        return len(self.sentence)

    def getNumWords(self):
        return len(self.getWords())

    def makeCaps(self):
        self.sentence = self.sentence.upper()
        return self.sentence

    def addPunct(self, punct_mark):
        self.sentence += punct_mark
        return self.sentence


test = "this is a very long sentence"
mysentence = sentence(test)
print(mysentence.addPunct("!"))



# EXERCISES PG 338
# class Sentence:
#     def __init__(self, a_sentence):
#         self.sen_list_words = a_sentence.split(' ')
#
#     #Methods
#     def getSentence(self):
#         string = ""
#         for i in range(len(self.sen_list_words)):
#             string = string + self.sen_list_words[i] + " "
#         return string
#
#     def getWords(self):
#         return self.sen_list_words
#
#     def getLength(self):
#         return len(self.getSentence())
#
#     def getNumWords(self):
#         return len(self.sen_list_words)
#
# mySentence = Sentence(test)
# print(mySentence.getNumWords())








