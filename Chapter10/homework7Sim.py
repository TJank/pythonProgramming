import homework7
from homework7 import Car

def createLetter():
    simpleletter = homework7.SimpleLetter("Mary", "John")

    simpleletter.addLine("Dear {0}, \nI'm sorry to say we must part. \nI wish you all the best. \nSincerely, \n{1}".format(simpleletter.getReceiver(),simpleletter.sender))
    simpleletter.getText()



createLetter()


def testStudent():
    bill = homework7.Student("Bill")

    print(bill.averageGPA())


testStudent()


def testCar():
    myHybrid = Car(50)

    myHybrid.addGas(20)
    myHybrid.drive(100)
    print(myHybrid.getGasLevel())

testCar()









