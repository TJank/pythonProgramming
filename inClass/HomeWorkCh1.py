import math
# Problem 1

#intBalance = 1000
#interestRate = 6/100

#A = input("Amount of change:")
#IA = int(A)
# how many quarters
#NQ = IA // 25
# how many dimes in what's left over
#IA = IA % 25
#ND = IA // 10
# how many nickels in what's left over
#IA = IA % 10
#NN = IA // 5
# how many pennies in what's left over
#IA = IA % 5
#print(A, "cents is", NQ, "quarters,", ND, "dimes,", NN, "nickels, and", IA, "pennies")

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




