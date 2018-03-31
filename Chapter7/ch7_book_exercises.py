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

# Listing 7.7
def readFile(filename):
    datafile = open(filename, "r")

    datadict = {}

    key = 0
    aline = datafile.readline()
    while aline != "":
        key = key + 1
        score = int(aline)
        datadict[key] = [score]

        aline = datafile.readline()

    return datadict

print(readFile("cs150exams.txt"))


# Exercises page 247
# 7.1
total = 5
while total < 50:
    total += 5

print(total)

#7.2
def numofSpaces(string):
    num_of_spaces = 0
    counter = 0

    while counter < len(string):
        if string[counter] == " ":
            num_of_spaces += 1
            counter += 1
        else:
            counter += 1

    return num_of_spaces

test_string = "Hello my name is bob . "

print(numofSpaces(test_string))

# 7.3
def averageScores():
    from numpy import mean
    score = 0
    score_list = []
    while score != "stop":
        score = input("Enter Exam score: ")
        score_list.append(score_list)

    return mean(score_list)

#print(averageScores())

# Listing 7.8 pg 248
def createCentroids(k, datadict):
    from random import randint
    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey = randint(1, len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1

    return centroids

def createClusters(k, centroids, datadict, repeats=10):
    for apass in range(repeats):
        print("****PASS", apass, "****")
        clusters = []
        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey], centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1])
        for clusterIndex in range(k):
            sums = [0] * dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
                for ind in range (len(sums)):
                    clusterLen = len(clusters[clusterIndex])
                    if clusterLen !=0:
                        sums[ind] = sums[ind]/clusterLen

                centroids[clusterIndex] = sums

        for c in clusters:
            print("CLUSTER")
            for key in c:
                print(datadict[key], end=" ")
            print()

    return clusters

test_clusters = [34,56,12,44,87,45,76,98,25,34,76,12,78,98,78,90,89,45,77,22,11,46,72,15,38,79,85,84,51,91]
_centroids = createCentroids(4, test_clusters)
print(_centroids)
print(createClusters(4 , _centroids, test_clusters, 10))






