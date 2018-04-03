# Homework 6
# Problem 1. (NEED TUTORING)
import math
import numpy as np

def euclidean_distance(x, y):
    """Dimensions of x and y must be the same."""

    dist = 0
    # checks if x is in one dimension
    if isinstance(x, (int,float)):
        return abs(x-y)
    else:
        dimension = len(x)
        for i in range(dimension):
            dist += (x[i] - y[i]) **2

        return np.sqrt(dist)

# v1 = [3, 45, 7, 2]
# v2 = [2, 54, 13, 15]
# print(euclidean_distance(v1,v2), "EUCLIDEAN DISTANCE")
def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

# v1 = [3, 45, 7, 2]
# v2 = [2, 54, 13, 15]
# print(cosine_similarity(v1,v2), "COSINE SIMILARITY")


# Problem 2.
# DOESNT WORK, ERROR FOR CENTROID
# Centroid: for points x1, x2 ..., xm in n-dimensions

def centroid(points):
    """All points must be of the same dimensions"""
    if isinstance(points[0], (int,float)):
        print(points[0], "POINTS AT 0")
        return np.mean(points)
    else:
        dimension = len(points[0])
        _centroid = [None] * dimension
        for i in range(dimension):
            num = 0
            for p in points:
                num += p[i]
            average = num/len(points)
            _centroid[i] = round(average, 2)

        return tuple(_centroid)





def kMeans(data, k, repitions=10):
    """
    Clusters will be represented as a list of lists or the form [c, A]
    where c is the centroid of a cluster and A is the collection of points
    in that cluster.
    :param data: collection of points
    :param k: number of desired clusters
    :param repitions: number of times to repeat the process of finding clusters
    :return: list of clusters of the form [c, A]
    """
    clusters = []

    # 1. Select k > 0: its done since k is a parameter of the function

    # 2. Randomly choose k data points to represent the centroids of k clusters
    from random import choice

    while len(clusters) < k:
        _centroid = choice(data)
        if not _centroid in [c[0] for c in clusters]:
            clusters.append([_centroid, []])

    #print(clusters)

    # 3. Repeat n times (repition)
    for i in range(repitions):
        # 3.1 for each data point p in data
        for p in data:
            # 3.1.1 Calculate the distance between p and all centroids
            distances = []
            for c, A in clusters:
                dis = cosine_similarity(p, c)
                distances.append((dis, c))
            closest_centroid = sorted(distances)[0][1]

            #print(p, closest_centroid)

            # 3.1.2 Assign p to the cluster with the closest centroid to p
            for c, A in clusters:
                if c == closest_centroid:
                    A.append(p)

            #print(clusters)

        # 3.2 Recalculate centroids for all clusters
        # Substitute the centroids for all clusters and flush the clusters
        for c in clusters:
            c[0] = centroid(c[1])       # calculate new centroids
            if i < repitions - 1:
                c[1] = []

        print(i, clusters)

    # 4. Return clusters
    return clusters

#data = [(1,5),(2,3),(5,7),(6,2)]
data = [(4,3,8,1),(8,5,6,9),(2,7,8,5),(1,8,6,3)]
print(kMeans(data, 2, 6), "K Cluster")


# Problem 3.
from random import random
def fillWithRandomNumbers(values):
    numbers = []

    for i in range(values):
        new_value = random()
        numbers.append("{0:.2f}".format(new_value*100))

    return numbers

print(fillWithRandomNumbers(5))


# Problem 4. (NEED TUTORING) doesnt work

def matrix_perfSq():
    matrix = []
    read_file = open("matrix.txt", "r")

    for aline in read_file:
        aline = aline.strip("\n")
        aline = aline.split(',')
        for i in range(len(aline)):
            aline[i] = int(aline[i])

        matrix.append(aline)
    count =0
    for i in range(1,17):
        for j in range(4):
            if not i in matrix[j]:
                count += 1
        if count == 4:
            print(i, "is not in matrix")
            count = 0

    row_sum = 0
    for i in range(len(matrix)):
        row_sum += matrix[0][i]



    read_file.close()
    print(matrix)

print(matrix_perfSq())

# Problem 5.
problem5_list = [1, 2, (5,9), "bob", [0,0,0], 45, "cat"]
def rotate(a_list, direction):
    removed_el = None
    if direction == "right":
        removed_el = a_list.pop(-1)
        a_list.insert(0, removed_el)

    elif direction == "left":
        removed_el = a_list.pop(0)
        #print(removed_el)
        a_list.append(removed_el)

    return a_list

#print(rotate(problem5_list, "right"))
#print(rotate(problem5_list, "left"))


# Problem 6. (HELP IF TIME)
def neighborAverage(values,row,column):
    length = len(values)
    width = len(values[0])
    neighbors = 0
    _sum = 0
    if row-1 >= 0:
        _sum = _sum + values[row-1][column]
        neighbors = neighbors + 1
        if column - 1 >=0:
            _sum = _sum + values[row-1][column-1]
            neighbors = neighbors+1
        if column+1 < width:
            _sum = _sum + values[row-1][column+1]
            neighbors = neighbors +1
    if row + 1 < length:
        _sum = _sum + values[row+1][column]
        neighbors = neighbors + 1
        if column - 1 >= 0:
            _sum = _sum + values[row+1][column-1]
            neighbors = neighbors + 1
        if column + 1 < width:
            _sum = _sum + values[row + 1][column+1]
            neighbors = neighbors + 1
    if column - 1 >= 0:
        _sum = _sum + values[row][column-1]
        neighbors = neighbors + 1
    if column + 1 < width:
        _sum = _sum + values[row][column+1]
        neighbors = neighbors + 1

    return _sum/neighbors

values = [[1,2,3,4],[5,6,7,8,],[9,10,11,12]]
print(neighborAverage(values, 0,2))
#print(neighborAverage(values, 1,2))
#print(neighborAverage(values, 0,0))


# Problem 7.
# A. & B. List of lists
class_info = []
info_list = []
readfile = open("studentN_id_gpa.txt", "r")
for aline in readfile:
    #aline.split(",")
    info_list.append(aline.split(","))
    class_info = class_info + info_list

print(info_list)

# Problem 8. (NEED TUTORING)
matrix_one = [[2,5,3],
              [1,4,2],
              [3,2,1]]

matrix_two = [[2,5,3],
              [1,4,2],
              [3,2,1]]

def matrix_multi(matrix_A, matrix_B):
    result = [[0,0,0],
              [0,0,0],
              [0,0,0]]

    # Iterate through rows of matrix_A
    # Will be a range of 3
    for i in range(len(matrix_A)):
        # Iterate through columns of matrix_B
        for j in range(len(matrix_B[i])):
            # Iterate through rows of matrix_B
            for k in range(len(matrix_B)):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
                #print(matrix_A[i][k],matrix_B[k][j])


    return result



print(matrix_multi(matrix_one, matrix_two))





# Own K-Cluster algorithim
def kmeans(dataSet,k):
    numFeatures = dataSet.getNumFeatures()
    centroids = getRandomCentroids(numFeatures,k)

# alist = [5,4,3,2,10]
# print(alist.sort())


