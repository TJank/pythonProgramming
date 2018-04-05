# Define a 2-dimensional point object

class Point(object):
    # Constructor Method
    def __init__(self,x,y):
        self.X = x
        self.Y = y

    # String representation of the object GOES OVER PRINT COMMAND WHERE PRINT IS LOCATION IN MEMORY
    def __repr__(self):
        return "({0},{1})".format(self.X, self.Y)


    def distance(self, a_point):
        return ((self.X - a_point.X)**2 + (self.Y - a_point.Y)**2) **(1/2)




# FOR TESTING A MODULE
if __name__ == "__main__":
    # Code below, only executes if the module is executed,
    # but not if it's imported
    point1 = Point(6, 9)
    print(point1.X)
    print(point1.Y)

    point2 = Point(1, 2)
    print(point2.X)
    print(point2.Y)

    print(point1, point2)

    d = point1.distance(point2)
    d1 = point2.distance(point1)
    print(d, d1)

