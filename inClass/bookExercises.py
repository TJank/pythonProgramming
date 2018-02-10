# CH 1 pg 14
pi = 3.14
r = 1
volume = (4/3) * pi * (r * r * r)
print(volume)

onePoint9 = 15 * (1/3)
print(onePoint9)

milesInLY = 5.878e+12
andromeda = 2.9e+6 * milesInLY
print(andromeda)


# CH 2 pg 56
#acc = 0
#for x in range(0, 100, 2):
   # acc = acc + x
   # print(acc)

#acc2 = 0
#for i in range(1, 50, 2):
    #acc2 = acc2 + i
   # print(acc2)

total = 0
for y in range(1, 101, 2):
    total = total + y
print(total)
FT = total / 100
print(FT)

#Page 60
def wallis(pairs):
    acc = 1
    num = 2

    for apair in range(pairs):
        leftterm = num/(num - 1)
        rightterm = num/(num + 1)

        acc = acc * leftterm * rightterm

        num = num + 2

    pi = acc * 2
    print(pi)

wallis(100000)

# pg 72
answer = 0
result = 99

if(result == 100):
    answer = 1
    print(answer)
else:
    answer = 2
    print(answer)

gradepoint = 0
score = 85

if(score > 90):
    gradepoint = 4
    print(gradepoint)
elif(80 < score < 89):
    gradepoint = 3
    print(gradepoint)
elif(70 < score < 79):
    gradepoint = 2
    print(gradepoint)
elif(60 < score < 69):
    gradepoint = 1
    print(gradepoint)
else:
    gradepoint = 0


def leapYear(year):
    if(year % 4 == 0):
        print(True)
        return True
    else:
        return False

def costOfOranges(pounds):
    cost = 0
    shipping = 7.50

    if(pounds >= 100):
        shipping = shipping - 1.5

    cost = pounds * .32 + shipping
    print(cost)

costOfOranges(100)

def threeIntegers(num, number, number1):
    if(num > number and num > number1):
        print(num)
    elif(number > num and number > number1):
        print(number)
    elif(number1 > num and number1 > number):
        print(number1)

def income(wage, hours):
    if(hours > 40):
        ot = hours - 40
        otpay = ot * (wage * 1.5)
        hours = 40
        pay = wage * hours + otpay
        print(pay)
    else:
        pay = wage * hours
        print(pay)























