
# A generic Vehicle Superclass

class Vehicle(object):
    def __init__(self, numberOfTires=0):
        self.numberOfTires = numberOfTires

    def __repr__(self):
        return "Tires: {0}".format(self.numberOfTires)

    def getDescription(self):
        return "A Vehicle with {0} tires.".format(self.numberOfTires)


class Car(Vehicle):
    def __init__(self, frontTrunk=False):
        super().__init__(4)
        self.hasFrontTrunk = frontTrunk

    def __repr__(self):
        return "({0} tires, {1})".format(self.numberOfTires, self.hasFrontTrunk)

    def getDescription(self):
        description = super().getDescription()
        return description + " and hasFrontTrunk={0}".format(self.hasFrontTrunk)


aVehicle = Vehicle()
print(aVehicle)
print(aVehicle.getDescription())
aCar = Car()
print(aCar)
print(aCar.getDescription())




