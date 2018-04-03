# Cluster Analysis
import numpy as np

# Euclidean distance: for points x, y in n-dimensions
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

# one dimension
p1 = 3
p2 = 5
# # print(euclidean_distance(p1,p2))
#
# # Two dimensions
# p1 = (3,4)
# p2 = (1,2)
# #print(euclidean_distance(p1,p2))
#
# # Five Dimensions
# p1 = (3,5,6,7,9)
# p2 = (3.1, 6.4,7.0,8.3,10.3)
# #print(euclidean_distance(p1,p2))

v1 = [3, 45, 7, 2]
v2 = [2, 54, 13, 15]
print(euclidean_distance(v1,v2))



# Centroid: for points x1, x2 ..., xm in n-dimensions

def centroid(points):
    """All points must be of the same dimensions"""
    if isinstance(points[0], (int,float)):
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

points = [(1.1,2.1,3.1,4),(7,6,0,7), (8.1, 4.7, 5.6, 3.2)]
#print(centroid(points))

#points = [1,5,7,8,6,7,1,3]
#print(centroid(points))



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
                dis = euclidean_distance(p, c)
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




#data = [1,5,2,3,7,6,1,2,5,3]
#kMeans(data, 3, 4)

#data = [(1,5),(2,3),(5,7),(6,2)]
#kMeans(data, 2,1)
data = [4.3, 5.2, 5.0, 4.8, 4.6, 5.0, 4.7, 4.8, 4.9, 5.1, 4.8, 4.5, 4.8, 5.0, 4.7, 4.7, \
        4.7, 4.8, 4.8, 4.8, 6.0, 5.1, 5.2, 5.1, 4.8, 4.7, 5.0, 4.9, 5.0, 4.8, 4.7, 4.8, \
        4.9, 5.7, 5.6, 4.9, 5.3, 5.8, 5.2, 5.3, 6.4, 5.8, 4.9, 4.9, 4.8, 4.9, 4.9, 4.3, \
        4.4, 5.7, 4.9, 4.9, 4.9, 6.1, 4.7, 5.0, 5.3, 5.5, 4.4, 4.9, 5.0, 5.2, 4.9, 5.1, \
        5.0, 5.4, 4.7, 5.2, 4.6, 5.0, 5.0, 5.0, 4.8, 4.9, 4.6, 5.0, 5.2, 4.8, 4.7, 4.9, \
        4.7, 4.9, 5.1, 5.1, 5.0, 4.7, 4.5, 4.8, 4.8, 4.8, 5.0, 4.9, 2.9, 5.5, 5.5, 5.1, \
        5.2, 5.1, 5.0, 5.3, 5.1, 5.0, 4.7, 5.2, 5.5, 5.1, 5.3, 5.3, 4.8, 5.7, 5.8, 5.6, \
        2.6, 5.0, 5.2, 4.8, 4.9, 4.9, 4.8, 5.2, 6.8, 6.2, 5.2, 6.0, 5.1, 6.1, 5.7, 5.4, \
        4.8, 5.1, 5.5, 5.0, 5.0, 5.0, 3.0, 5.4, 5.3, 5.1, 5.1, 4.9, 5.3, 5.0, 4.9, 5.4, \
        5.8, 5.3, 5.0, 4.6, 4.9, 4.7, 2.9, 5.2, 4.8, 5.4, 5.1, 5.5, 5.1, 5.5, 6.3, 6.6, \
        3.2, 5.2, 5.5, 5.5, 6.1, 6.2, 4.9, 5.1, 4.9, 4.9, 5.9, 5.7, 4.7, 5.0, 5.4, 5.1, \
        5.0, 5.5, 4.8, 5.0, 5.0, 4.8, 5.0, 5.0, 5.5, 5.3, 5.0, 5.0, 5.0, 5.4, 4.9, 5.2, \
        5.6, 6.2, 5.0, 5.8, 5.4, 5.1, 5.4, 5.1, 2.6, 5.2, 5.5, 4.9, 5.2, 5.3, 5.6, 4.9, \
        5.6, 5.1, 2.5, 5.8, 5.1, 5.3, 5.3, 5.4, 5.6, 5.3, 5.2, 5.2, 5.3, 3.3, 5.9, 5.1, \
        5.5, 5.1, 5.8, 5.8, 6.5, 5.7, 5.5, 5.5, 5.5, 5.6, 5.1, 3.2, 5.0, 5.5, 5.3, 5.9, \
        5.6, 6.0, 5.2, 5.5, 2.5, 5.2, 5.4, 3.0, 2.9, 2.6, 2.6, 5.5, 2.8, 5.4, 2.5, 2.5, \
        3.3, 5.2, 4.6, 5.4, 5.5, 5.9, 6.1, 6.5, 6.2, 6.2, 5.5, 5.9, 5.6, 5.7, 5.8, 5.9, \
        4.4, 6.1, 6.1, 6.3, 5.9, 5.8, 6.3, 6.3, 7.1, 3.3, 6.8, 6.4, 6.4, 8.9, 3.4, 4.8, \
        4.5, 2.6, 2.9, 2.5, 2.8, 2.5, 4.0, 5.3, 4.9, 4.7, 2.8, 2.5, 5.0, 3.4, 6.5, 5.2, \
        3.2, 4.7, 4.7, 4.6, 2.7, 2.8, 5.1, 2.7, 5.2, 4.8, 5.7, 3.1, 4.8, 4.2, 3.2, 2.5, \
        2.5, 5.4, 4.6, 4.6, 2.8, 2.9, 5.0, 2.9, 4.8, 5.4, 2.6, 2.6, 6.5, 6.1, 4.9, 3.5, \
        6.0, 2.5, 3.7, 6.1, 4.9, 2.5, 2.5, 2.8, 4.8, 5.3, 3.2, 5.1, 5.0, 2.8, 2.6, 4.7, \
        5.1, 3.5, 4.7, 2.6, 4.8, 3.3, 5.3, 5.1, 5.0, 5.1, 4.9, 2.9, 4.7, 5.3, 5.7, 5.2, \
        3.0, 4.8, 5.2, 2.5, 5.0, 5.2, 5.6, 7.2, 4.6, 4.7, 4.9, 2.9, 4.9, 2.7, 4.8, 3.1, \
        2.6, 4.4, 2.8, 2.7, 4.8, 4.3, 3.1, 4.3, 4.3, 2.5, 3.2, 2.5, 2.6, 4.7, 3.6, 2.6, \
        4.6, 4.4, 2.6, 2.7, 5.0, 5.0, 2.8, 2.8, 2.6, 5.2, 2.5, 2.7, 2.7, 3.0, 2.6, 3.2, \
        3.4, 4.1, 2.5, 3.3, 4.9, 4.7, 5.0, 4.9, 4.6, 2.7, 2.5, 2.5, 4.5, 2.7, 2.5, 3.9, \
        3.3, 6.6, 5.4, 3.0, 4.9, 4.8, 2.6, 4.6, 2.6, 4.9, 3.6, 6.5, 2.8, 3.0, 4.5, 2.5, \
        3.1, 4.8, 4.9, 6.2, 4.7, 4.7, 4.3, 5.0, 2.7, 4.5, 4.2, 2.8, 4.4, 4.3, 4.9, 4.6, \
        4.5, 3.6, 2.6, 4.8, 3.0, 4.2, 3.0, 5.1, 2.5, 2.6, 2.6, 2.5, 2.5, 4.7, 2.6, 4.4]

#kMeans(data, 6, 100)















