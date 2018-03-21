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
print(euclidean_distance(p1,p2))

# Two dimensions
p1 = (3,4)
p2 = (1,2)
print(euclidean_distance(p1,p2))

# Five Dimensions
p1 = (3,5,6,7,9)
p2 = (3.1, 6.4,7.0,8.3,10.3)
print(euclidean_distance(p1,p2))



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

points = [(1.1,2.1,3.1,4),(7,6,0,7),(8.1,4.7,5.6,3.2)]
print(centroid(points))

points = [1,5,7,8,6,7,1,3]
print(centroid(points))





















