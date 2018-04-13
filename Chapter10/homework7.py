

# Problem 1

class SimpleLetter(object):
    def __init__(self, letterFrom, letterTo):
        self.receiver = letterTo
        self.sender = letterFrom



    def addLine(self, line):
        self.writeFile.write(line)








# Problem 2
class Student(object):
    def __init__(self, s_name):
        self.name = s_name
        self.totalQuizScore = 0
        self.numQuizes = len(self.quizScoreList)
        self.quizScoreList = []

    def getName(self):
        return self.name

    def addQuiz(self, quizscore):
        self.quizScoreList.append(quizscore)

    def getTotalScore(self):
        for i in range(len(self.quizScoreList)):
            self.totalQuizScore += self.quizScoreList[i]

        return self.totalQuizScore

    def getAverage(self):
        return self.totalQuizScore // self.numQuizes


