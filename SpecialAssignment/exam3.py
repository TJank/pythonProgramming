# Exam 3: Tyler Jankowski IT210

import datetime


# Problem 1.
class Message(object):
    def __init__(self, sender, recipient):
        self.personFrom = sender
        self.personTo = recipient
        self.messageBody = []

    def addLine(self, alineOfText):
        self.messageBody.append(alineOfText)

    def toString(self):
        toString = ""
        toString += "From: {0}\n".format(self.personFrom)
        toString += "To: {0}\n".format(self.personTo)
        for i in range(len(self.messageBody)):
            toString += self.messageBody[i] + "\n"

        return toString


class Mailbox(object):
    def __init__(self):
        self.messages = []

    def addMessage(self, amessage):
        self.messages.append(amessage)

    def getMessage(self, an_index):
        print(self.messages[an_index].toString())

    def removeMessage(self, an_index):
        self.messages.pop(an_index)


testM = Message("Morgan Freeman","The President")
testM.addLine("This is the president.")
testM.addLine("You have an amazing voice.")
testM.addLine("Come chill at the White House one day.")
myMailbox = Mailbox()
myMailbox.addMessage(testM)
myMailbox.getMessage(0)

# Problem 2.

class LinearEquation(object):
    def __init__(self, mValue, bValue):
        self.m = mValue
        self.b = bValue
        self.name = None

    def getM(self):
        return self.m

    def getB(self):
        return self.b

    def __repr__(self):
        return "This is the Linear Equation: y = {0}x + {1}".format(self.m, self.b)

    def setName(self, letter):
        self.name = letter

    def __str__(self):
        return self.name

    def value(self, xValue):
        y = self.m * xValue + self.b
        return y

    def compose(self, a_2nd_linearEquation):
        newM = self.m * a_2nd_linearEquation.getM()
        newB = (self.m * a_2nd_linearEquation.getB()) + self.b
        return "y({0}) = {1}x + {2}".format(a_2nd_linearEquation, newM, newB)

    def __add__(self, other):
        newM = self.m + other.getM()
        newB = self.b + other.getB()
        return "y + {0} = {1}x + {2}".format(other, newM, newB)

y = LinearEquation(2,1)
z = LinearEquation(2,5)
y.setName("y")
z.setName("z")
print(y.value(5))
print(y.compose(z))
print(y.__add__(z))


# Problem 3.
class Customer(object):
    def __init__(self):
        self.totalAmount = 0
        self.discount = False
        self.newPurchase = 0


    def makePurchase(self, amount):
        self.newPurchase = amount
        if self.discount:
            self.newPurchase -= 10
            self.discount = False
            self.totalAmount += amount
            return "Your total is ${0}, you saved $10".format(self.newPurchase)
        else:
            self.totalAmount += amount
            return "Your total is ${0}".format(self.newPurchase)

    def discountReached(self):
        #print(self.totalAmount)
        if self.totalAmount >= 100:
            self.totalAmount = 0
            self.discount = True

me = Customer()
print(me.makePurchase(100))
me.discountReached()

print(me.makePurchase(90))
print(me.makePurchase(40))
me.discountReached()
print(me.makePurchase(50))



# Problem 4.
class Appointment(object):
    def __init__(self, year, month, day, des):
        self.date = datetime.date(year,month,day)
        self.description = des

    def getDescription(self):
        return self.description

    def occursOn(self, year, month, day):
        if self.date == datetime.date(year, month, day):
            return True
        else:
            return False

class Daily(Appointment):
    def __init__(self, year, month, day, des):
        super().__init__(year, month, day, des)

    def occursOn(self, year, month, day):
        return True

class Monthly(Appointment):
    def __init__(self, year, month, day, des):
        super().__init__(year, month, day, des)

    def occursOn(self, year, month, day):
        if self.date.day == day:
            return True
        else:
            return False

class OneTime(Appointment):
    def __init__(self, year, month, day, des):
        super().__init__(year, month, day, des)




def createNewApp():
    type1 = input("What type of Appointment? (OneTime,Daily,Monthly)")
    if type1 == "OneTime":
        type1 = OneTime
    elif type1 == "Daily":
        type1 = Daily
    elif type1 == "Monthly":
        type1 = Monthly


    month = int(input("What month should we schedule it for?"))
    day = int(input("What day should we schedule it for?"))
    year = 2018
    des = input("Enter a description:")

    return type1(year, month,day, des)


def testAppointment():
    appointments = []
    appointments.append(OneTime(2018,7,16, "Dentist"))
    appointments.append(Daily(2018,4,29, "Back Stretches"))
    appointments.append(Daily(2018,9,25, "Go to school"))
    appointments.append(Monthly(2018,1,5, "Meds check up"))
    appointments.append(OneTime(2018,7,16, "Broken Arm"))

    # User Friendly Verson of Creating Appointments
    appointments.append(createNewApp())

    month = int(input("Enter Month: "))
    day = int(input("Enter Day: "))
    year = int(input("Enter Year: "))


    for app in appointments:
        if app.occursOn(year, month, day):
            print(app.getDescription())



testAppointment()




# Problem 5.



