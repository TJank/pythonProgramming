class Student(object):
    def __init__(self, s_name):
        self.name = s_name
        self.totalQuizScore = 0
        self.quizScoreList = []
        self.numQuizes = 0

        self.classes = []
        self.grades = []
        self.totalgpa = 0

    def getName(self):
        return self.name

    def getNumQuizes(self):
        return self.numQuizes

    def addQuiz(self, quizscore):
        self.quizScoreList.append(quizscore)
        self.totalQuizScore += quizscore
        self.numQuizes += 1

    def getTotalScore(self):
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

def testStudent():
    Tyler = Student("Tyler")

    Tyler.addQuiz(85)
    Tyler.addQuiz(72)
    Tyler.addQuiz(94)
    Tyler.addQuiz(50)
    Tyler.addQuiz(68)

    print(Tyler.getName())
    print(Tyler.getAverage())
    print(Tyler.getNumQuizes())
    print(Tyler.getTotalScore())




testStudent()
