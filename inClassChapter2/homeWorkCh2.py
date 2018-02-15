import random
import math
# Question 1
#part 1
part1 = 0
for i in range(0,101,2):
    part1 += i
print(part1)

# part 2
part2 = 0
for i in range(1,101):
    part2 += i ** 2
print(part2)

# part 3
acc = 1
for i in range(0,21):
    acc *= 2 ** i
    #print(i)
print(acc)

# part 4
part4 = 1
a = int(input("Please input a number."))
b = int(input("Please input a second number."))
for i in range(a,b + 1,1):
    if not i % 2 == 0:
        part4 *= i
        print(i)

print(part4)

#part 5
part5 = 0
input1 = input("Please enter 5 or more numbers.")
for num in input1:
    if not int(num) % 2 == 0:
        part5 += int(num)
print(part5)

# Question 2
def rockPaperS(mypick):
    rps = random.randrange(0, 3)
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    compChoice = ""

    if(rps == 0):
        compChoice = rock
        print("You picked " + mypick + " and the computer picked " + compChoice + ".")
    elif(rps == 1):
        compChoice = paper
        print("You picked " + mypick + " and the computer picked " + compChoice + ".")
    elif(rps == 2):
        compChoice = scissors
        print("You picked " + mypick + " and the computer picked " + compChoice + ".")
    else:
        print("I forgot to pick one..")


rockPaperS("rock")

# Question 3
a = 32310901
b = 1729
m = 2**24


# Question 4
def pred_vs_prey():
    A = float(input("Enter rate at which prey birth exceeds natural death."))
    B = float(input("Enter rate of predation."))
    C = float(input("Enter rate which predator deaths exceed births without food."))
    D = float(input("Enter rate predator increase in presence of food."))
    inPopSizePrey = int(input("Enter initial population size for prey."))
    inPopSizePred = int(input("Enter initial population size for predator."))
    numPeriods = int(input("Enter number of periods."))

    preyn = inPopSizePrey * (1 + A - B * inPopSizePred)
    predn = inPopSizePred * (1 - C + D * inPopSizePrey)

    print(preyn)
    print(predn)

pred_vs_prey()

# Question 5
num = int(input("Enter an integer."))
counter = 2
prime_Test = False
while counter <= math.sqrt(num):
    if num % counter == 0:
        counter += 1
        prime_Test = True
    else:
        counter += 1
    if prime_Test == False:
        print("%s is prime!"%(num))
    else:
        print("%s is not a prime!"%(num))

# Question 6
def cardNumCheck():
    cardNum = input("Please enter your 8 digit card number.")
    slice1 = " " # starting with last digit
    slice2 = " " # starting with second to last digit

    flag = True

    for num in cardNum:
        if flag:
            slice2 += num
            flag = not flag
        else:
            slice1 += num
            flag = not flag

    sum = 0
    for i in range(0,len(slice1)+1):
        sum = int(slice1[i]) + sum
    print(sum)
    sum2 = 0
    holder = 0
    for i in slice2:
        holder = i * 2
        str(holder)
        sum2 += holder
    print(sum2)

cardNumCheck()

# Question 7
def common_multiples(X,Y,Z):
    multiX = []
    for i in range(0,10):
        cmnM = X * i
        multiX.append(cmnM)

    multiY = []
    for i in range(0,10):
        cmnM = Y * i
        multiY.append(cmnM)

    commonMultiples = []



common_multiples(4, 6, 30)

