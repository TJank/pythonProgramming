# Listing 7.1 pg 240
import math

def euclidD(point1, point2):
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total = total + diff

    euclidDistance = math.sqrt(total)
    return euclidDistance

def readFile(filename):
    datafile = open(filename, "r")
    datadict = {}

    key = 0
    for aline in datafile:
        key = key + 1
        score = int(aline)

        datadict[key] = [score]

    datafile.close()

    return datadict




