

# Problem 1

class SimpleLetter(object):
    def __init__(self, letterFrom, letterTo):
        self.receiver = letterTo
        self.sender = letterFrom



    def addLine(self, line):
        writeFile = open("Letter.txt", 'w')
        writeFile.write(line)
        writeFile.close()

    def getText(self):
        readFile = open("Letter.txt", 'r')
        for aline in readFile:
            print(aline)

        readFile.close()

    def getSender(self):
        return self.sender

    def getReceiver(self):
        return self.receiver










# Problem 2
class Student(object):
    def __init__(self, s_name):
        self.name = s_name
        self.totalQuizScore = 0
        self.quizScoreList = []
        self.numQuizes = 0

        self.classes = ["Biology", "Calculus", "History"]
        self.grades = ["A", "B", "C"]
        self.totalgpa = 0

    def getName(self):
        return self.name

    def addQuiz(self, quizscore):
        self.quizScoreList.append(quizscore)
        self.numQuizes += 1

    def getTotalScore(self):
        for i in range(len(self.quizScoreList)):
            self.totalQuizScore += self.quizScoreList[i]

        return self.totalQuizScore

    def getAverage(self):
        return self.totalQuizScore // self.numQuizes

    def addClassAndGPA(self, className, classGrade):
        self.classes.append(className)
        self.grades.append(classGrade)

    def averageGPA(self):
        gpa_dict = {"A+": 4.33, "A": 4.00, "A-": 3.67, "B+": 3.33, "B": 3.00, "B-": 2.67, "C+": 2.33,
                    "C": 2.00, "C-": 1.67, "D+": 1.33, "D": 1.00, "D-": .67, "F": 0.00}

        gpa_keys = gpa_dict.keys()

        for i in range(len(self.grades)):
            one_grade = self.grades[i]
            gpa = gpa_dict[one_grade]
            self.totalgpa += gpa

        return self.totalgpa // len(self.grades)

#Problem 3

class Car(object):
    def __init__(self, efficiency):
        self.gasLevel = 0
        self.efficiency = efficiency

    def addGas(self, gallons):
        self.gasLevel = gallons

    def getGasLevel(self):
        return self.gasLevel

    def drive(self, miles):
        self.gasLevel = self.gasLevel - (miles // self.efficiency)


# Problem 4.
class Patient(object):
    def __init__(self, id, name, gender, age, height, weight, dob):
        self.id = id
        self.name = name
        self.gener = gender
        self.age = age
        self.height = height
        self.dob = dob
        self.weight = weight
        self.phoneNum = 0
        self.address = ""

    def setID(self, changedItem):
        self.id = changedItem
    def setname(self, changedItem):
        self.name = changedItem
    def setgener(self, changedItem):
        self.gener = changedItem
    def setage(self, changedItem):
        self.age = changedItem
    def setheight(self, changedItem):
        self.height = changedItem
    def setdob(self, changedItem):
        self.dob = changedItem
    def setweight(self, changedItem):
        self.weight = changedItem
    def setphoneNum(self, changedItem):
        self.phoneNum = changedItem
    def setaddress(self, chnagedItem):
        self.address = chnagedItem

    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getGener(self):
        return self.gener
    def getage(self):
        return self.age
    def getheight(self):
        return self.height
    def getdob(self):
        slice1 = self.dob[0:2]
        secSlice = self.dob[2:4]
        third = self.dob[4:]
        return "{0}/{1}/{2}".format(slice1,secSlice,third)
    def getweight(self):
        return self.weight
    def getphoneNum(self):
        slice1 = self.dob[0:3]
        secSlice = self.dob[3:6]
        third = self.dob[6:]
        return "{0}-{1}-{2}".format(slice1, secSlice, third)
    def getaddress(self):
        return self.address
    

# Problem 5.
class Color(object):
    def __init__(self, redINT, greenINT, blueINT):
        if not (0  < redINT and redINT < 1):
            print("ERROR: Value must be between 0 and 1")
        else:
            self.red = redINT

        if not (0  < greenINT and greenINT < 1):
            print("ERROR: Value must be between 0 and 1")
        else:
            self.green = greenINT

        if not (0  < blueINT and blueINT < 1):
            print("ERROR: Value must be between 0 and 1")
        else:
            self.blue = blueINT

        self.color = 0

    def addColors(self):
        self.color = self.red + self.green + self.blue
        if self.color > 1:
            self.color = 1
        if self.color < 0:
            self.color = 0
        return self.color

    def subtractColors(self):
        self.color = self.red - self.green - self.blue
        if self.color > 1:
            self.color = 1
        if self.color < 0:
            self.color = 0
        return self.color








