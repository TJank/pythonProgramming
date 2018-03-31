# Code for Chapter 4 homework
# Problem 1.
import turtle
import numpy as np
import matplotlib.pyplot as plt
from random import gammavariate

def randomList_gamma(n, a, b):
    randomList = []
    for i in range(n):
        rand = float("{0:.1f}".format(gammavariate(a, b)))
        randomList.append(rand)
    return randomList

rand_list = randomList_gamma(1000, 2, 2)
print(rand_list)

points = rand_list
bins = int(np.max(rand_list) - np.min(rand_list))
#print(bins)
fig, ax = plt.subplots()
_mean = np.mean(points)
_std = np.std(points)

plt.hist(points, bins, histtype='bar', rwidth=0.8)
# Best fit line???
#y = ((1 / (np.sqrt(2*np.pi) * _std)) * np.exp(-0.5 * (1 / _std * (bins - _mean)) **2))
#ax.plot(bins, y, '--')
plt.xlabel('List Value')
plt.ylabel('Frequency')
plt.title('Histogram of randomList_gamma: Mean: {0:.2f}, STD: {1:.2f}'.format(_mean,_std))
plt.legend()
plt.show()




# Problem 2.
L1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
L2 = [11, 11, 7, 9, 16, 4, 1]

def sameSet(list, list2):
    copy_list1 = []
    copy_list2 = []

    list.sort()
    list2.sort()

    for i in range(len(list) - 1):
        if not list[i] in copy_list1:
            copy_list1.append(list[i])
    #print(copy_list1)

    for i in range(len(list2) - 1):
        if not list2[i] in copy_list2:
            copy_list2.append(list2[i])
    #print(copy_list2)

    if copy_list1 == copy_list2:
        return "These are the same set."
    else:
        return "These are not a same set."

#print(sameSet(L1,L2))

# Problem 3.
listofnum = [i for i in range(11)]
#print(listofnum)
def sumList(list):
    # check if list is odd
    # git middle number
    midNum = 0
    if len(list) % 2 != 0:
        midIdx = len(list) // 2
        midNum = list[midIdx]

    # Create new list
    sumList = []
    # Get number of additions
    times = len(list) // 2
    count = 0
    for i in range(times):
        sum = list[count] + list[count + 1]
        sumList.append(sum)
        count += 2

    mid = len(sumList) // 2
    sumList.insert(mid, midNum)

    return sumList

#print(sumList(listofnum))

# Problem 4.
bob = turtle.Turtle()
points = [(1,2),(3,1),(7,9),(9,2),(5,5)]

def plotRegression(points):
    x_list = [x[0] for x in points]
    y_list = [y[1] for y in points]
    #print(x_list, y_list)
    #print(sum(x_list), sum(y_list))

    x_bar = sum(x_list) / len(x_list)
    y_bar = sum(y_list) / len(y_list)
    n = len(x_list)
    sum1 = 0

    m = ((sum(x_list) * sum(y_list)) - (n * x_bar * y_bar)) / (((sum(x_list))**2) - (n * (x_bar**2)))
    #print(m)
    #y = y_bar + (m * (x - x_bar))
    for i in range(len(x_list)):
        sum1 += x[i] * y[i]

    #sum1 = sum([x[1] * y[i] for i in range(len(x_list))])


plotRegression(points)
# Problem 5.
def gcd(x, y):
    x1 = abs(min(x, y))
    y1 = abs(max(x, y))
    gcd_ = x1

    if y1 % x1:
        gcd_ = gcd(x1, y1 % x1)
    return gcd_

def fracAdd(frac1, frac2):
    a = frac1[0]
    b = frac2[1]
    c = frac2[0]
    d = frac2[1]
    numerator = a*d + b*c
    denominator = c*d
    g = gcd(numerator, denominator)
    return (numerator/g, denominator/g)

#print(gcd(4,5))
import fractions
def addFractions(frac1, frac2):
    x1, y1 = frac1[0], frac1[1]
    x2, y2 = frac2[0], frac2[1]
    print(fractions.Fraction(x1, y1) + fractions.Fraction(x2, y2))

    # Get greatest common denominator
    #print(gcd(y1, y2))

def multiplyFractions(frac1, frac2):
    x1, y1 = frac1[0], frac1[1]
    x2, y2 = frac2[0], frac2[1]
    print(fractions.Fraction(x1, y1) * fractions.Fraction(x2, y2))


fraction1 = (1,4)
fraction2 = (2,5)

#print(addFractions(fraction1, fraction2))

# Problem 6.
list1 = [i for i in range(1,10)]
list2 = [100,200]

def transform(list1,list2,r1,r2):
    transform_list = list1[r1:r2]
    for i in range(len(transform_list)):
        insert = transform_list.pop(-1)
        list2.append(insert)
    return list2

print(transform(list1,list2,4,7))


# Problem 7.


# Problem 8.
morseAlphabet = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D" ,
    ".": "E" ,
    "..-.": "F" ,
    "--.":  "G" ,
    "....": "H" ,
    "..": "I",
    ".---": "J" ,
    "-.-": "K" ,
    ".-..": "L" ,
    "--" : "M",
    "-.": "N" ,
    "---": "O",
    ".--.":  "P" ,
    "--.-": "Q" ,
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U" ,
    "...-": "V" ,
    ".--": "W" ,
    "-..-": "X" ,
    "-.--": "Y",
    "--..": "Z",
    "/": " "
    }
testCode = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.-- "








def fromMorseCodeToWords(morseCode):



    decode_message = ""
    letter = ""

    for i in range(0, len(morseCode)):
        if morseCode[i] is " ":
            decode_message += morseAlphabet[letter]
            letter = ""
            continue
        else:

            letter += morseCode[i]

    return decode_message




#print(fromMorseCodeToWords(testCode))

# Problem 9.
txtabrvs = {"2F4U": "Too Fast For You",
            ("4YEO", "FYEO") : "For Your Eyes Only",
            "AAMOF" : "As a Matter of Fact",
            "AFK" : "Away from Keyboard",
            "AKA" : "Also known as",
            "BTW" : "By the Way",
            "B/C" : "Because",
            "FWIW" : "For what it's Worth",
            "FYI" : "For your Information",
            "FTW" : "For the Win",
            "HF" : "Have fun",
            "HTH" : "Hope this Helps",
            "IDK" : "I don't know"}

text_message = "FYI we won the game. I shouted out FTW as I scored."


def txtmsg_to_english(textMessage):
    plain_text = ""
    word = ""

    for i in range(len(textMessage)):
        if textMessage[i] is " ":
            if word in txtabrvs.keys():
                plain_text += " " + txtabrvs[word]
                word = ""
                continue
            else:
                plain_text += " " + word
                word = ""
                continue
        else:
            word += textMessage[i]

    return plain_text

print(txtmsg_to_english(text_message))























