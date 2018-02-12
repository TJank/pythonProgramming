import math





# Problem 1
def interest(months):
    acc = 1000
    IR = 0.06
    balance = 1000
    for i in range(1,months +1):
        acc = acc + (balance * IR)
        print("After month ", i, "your balance is: ", acc)

interest(3)

# Question 2
#cents = input("Amount of change:")
#IA = int(cents)
#Now number of quarters NQ
#NQ = IA // 25
#Get remainder after quarters
#IA = IA % 25
#How many dimes in whats remaining ND
#ND = IA // 10
#Get remainder
#IA = IA % 10
#Number of Nickles NN
#NN = IA // 5
#Number of pennies is remainder
#IA = IA % 5
#print(cents, "cents is", NQ, "quarters,", ND, "dimes,", NN, "nickles, and", IA, "pennies")

# Question 3
seconds = 50000
hours = seconds / 3600
hours = int(hours)
InitialA = seconds % 3600
minutes = InitialA / 60
minutes = int(minutes)
InitialA = InitialA % 60
sec = InitialA % 60
print(seconds, "seconds is", hours, "hours,", minutes, "minutes, and ", sec, "seconds.")

# Question 4
def threeAngles(a, b, c):
    angleA = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
    angleB = math.degrees(math.acos((c**2 + a**2 - b**2)/(2*a*c)))
    angleC = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
    print(angleA)
    print(angleB)
    print(angleC)
    print(angleC + angleB + angleA)

#threeAngles(3,7,9)

# Question 5
r = 6378 * 10**3
m1 = 5.9742 * 10**24
G = 6.67300 * 10**-11
m2 = int(input("Please enter your weight in Kilograms."))
print(r,m1,G)

gForce = (G * m1 * m2) / (r * r)
forceG = m2 * G

print(gForce)
print(forceG)

# Question 6
def drawStar(starSize):
    angle = 120

    for side in range(12):
        turtle.forward(starSize)
        turtle.right(angle)
        turtle.forward(starSize)
        turtle.right(30 - angle)

turtle.exitonclick()
# Question 7

# Question 8

# Question 9

# Question 10


