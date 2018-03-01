# Book exercises for chapter 4
# Session 4.1 pg 121
mylist = [3,"cat", 6.5, 2]
print(mylist)

# Session 4.2 pg 123
indx = mylist[2]
print(indx)
double = mylist + mylist
print(double)
triple = mylist*3
print(triple)
print(3 in mylist)
print("dog" in mylist)

# Session 4.3 pg 123
changelist = [1,2,"buckle my shoe", 3,4,"shut the door"]
print(changelist)
changelist[2] = "the sky is blue"
print(changelist)

# Session 4.4 pg 124
my_list = [1,2,3,4]
A = [my_list]*3
print(A)
my_list[2] = 45
print(A)

# Session 4.5 pg 125
#print(range(10))
#print(LISTISHERE(range(10)))
#print(LISTISHERE(range(10, 2, -2)))
#print(LISTISHERE("the quick fox"))

# Session 4.6 LIST METHODS pg 126
myList = [1024,3,True, 6.5]
myList.append(False)
#print(myList)
myList.insert(2,4.5)
#print(myList)
myList.pop()
#print(myList)
myList.pop(1)
#print(myList)
#print(myList.pop(2))
myList.sort()
#print(myList)
myList.reverse()
#print(myList)
#print(myList.count(6.5))
#print(myList.index(4.5))
myList.remove(6.5)
print(myList)

# Session 4.7 pg 127
a = "minnesota vikings"
#print(a.split())
#print(a.split('i'))
#print(a.split('nn'))

# Exercises PG 127
# 4.1
LISTISHERE = [7, 9, 'a', 'cat', False]
LISTISHERE.append(3.14)
LISTISHERE.append(7)
#print(LISTISHERE)
LISTISHERE.insert(3, 'dog')
#print(LISTISHERE.index('cat'))
count = LISTISHERE.count(7)
#print(count)
LISTISHERE.remove(7)
#print(LISTISHERE)
LISTISHERE.pop(2)
#print(LISTISHERE)

# 4.3
string = "the quick brown fox"
listOfWords = []
listOfWords.append(string[0:3])
listOfWords.append(string[4:9])
listOfWords.append(string[10:15])
#print(listOfWords)

mylist410 = [1,4,(1,2,3),10]

#print(mylist410)

# Session 4.8 pg 129
alist = [20,32,21,26,33,22,18]
#print(max(alist))
#print(min(alist))
#print(max('house'))
#print(min('house'))
#print(max(alist)- min(alist))

# listing 4.1 pg 130
def getRange(alist):
    return max(alist) - min(alist)

# Session 4.9
#print(getRange([2,4]))
#print(getRange(alist))

# Listing 4.2
def getMax(alist):
    maxSoFar = alist[0]
    for pos in range(1,len(alist)):
        if alist[pos] > maxSoFar:
            maxSoFar = alist[pos]

    return maxSoFar

# Exercises pg 131
# 4.14
def getMin(alist):
    minSoFar = alist[0]
    for i in range(1, len(alist)):
        if alist[i] < minSoFar:
            minSoFar = alist[i]

    return minSoFar

# 4.15
def getMinIt(alist):
    minSoFar = alist[0]
    for i in alist[1:]:
        if i < minSoFar:
            minSoFar = i

    return minSoFar

print(getMinIt([1000,3,10,5,.5]))

# 4.16
def getNewRange(alist):
    max = getMax(alist)
    min = getMinIt(alist)
    return max - min

print(getNewRange([100,5,52,65,7,2]))

# Listing 4.4 pg 131
# MEAN
def mean(alist):
    mean = sum(alist) / len(alist)
    return mean

print(mean(alist))

# Listing 4.5 pg 134
def median(alist):
    copylist = alist[:]
    copylist.sort()

    if len(copylist) % 2 == 0:      # even length
        rightmid = len(copylist)//2
        leftmid = rightmid - 2
        median = (copylist[leftmid] + copylist[rightmid]) / 2

    else:       # odd length
        mid = len(copylist)//2
        median = copylist[mid]

    return median

print(median(alist))

# Dictionaries pg 136
ages = {'David':45,'Brenda':46}
ages['Kelsey']=19
ages['Hannah']=16
ages['Rylea']=7
ages['David'] = ages['David'] + 1
#print(ages['David'])
#print(ages)
#print(len(ages))

# Session 4.14 pg 138
#print(ages.keys())
#print(list(ages.keys()))
#print(ages.get('Lena'))
#print('Rylea' in ages)

#print('-'*20)


names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10, 23, 13, 18, 12]

def makeDictionary(list1,list2):
    scoreDict = {list1[i]: list2[i] for i in range(len(list1))}
    return scoreDict['barb']


print(makeDictionary(names,scores))

# Listing 4.6

def mode(alist):
    countDict = {}

    for item in alist:
        if item in countDict:
            countDict[item] = countDict.get(item,0)+1
        else:
            countDict[item] = 1

    countlist = countDict.values()
    maxcount = max(countlist)

    modeList = []
    for item in countDict:
        if countDict[item] == maxcount:
            modeList.append(item)

    return modeList

print(mode([1,1,4,5,6,2,4,7,1,4,6,1]))

# Listing 4.8
# Compute a frequency table

def frequencyTable(alist):
    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1


    itemlist =[]        # BECAUSE list(countdict.keys()) does not work
    for item in countdict.keys():
        itemlist.append(item)

    print(itemlist)
    itemlist.sort()
    print("ITEM", "FREQUENCY")

    for item in itemlist:
        print(item, "  ", countdict[item])


a_list = [3,1,1,5,3,1,2,2,3,5,3,5,4,4,6,7,6,7,5,7,8,3,8,2,3,4,1,5,6,7]
frequencyTable(a_list)

# LIsting 4.9 pg 145
def frequencyTableAlt(alist):
    print("ITEM", "FREQUENCY")
    slist = alist[:]
    slist.sort()
    countlist = []

    previous = slist[0]
    groupCount = 0
    for current in slist:
        if current == previous:
            groupCount += 1
            previous = current
        else:
            print(previous, "   ", groupCount)
            previous = current
            groupCount = 1

    print(current, "   ", groupCount)

print("-"*20)
frequencyTable(a_list)


a_list = [3,1,1,5,3,1,2,2,3,5,3,5,4,4,6,7,6,7,5,7,8,3,8,2,3,4,1,5,6,7]
# Exercise 4.34 pg 145
def frequencyTableAlt1(alist):
    slist = alist[:]
    slist.sort()
    countlist = []

    previous = slist[0]
    groupCount = 0
    for current in slist:
        if current == previous:
            groupCount += 1
            previous = current
        else:
            countlist.append(("Item", previous))
            countlist.append(("Frequency", groupCount))
            previous = current
            groupCount = 1

    return countlist

print(frequencyTableAlt1(a_list))

# 4.35 pg 145
new_scores = [('john', 10), ('bob', 8), ('john', 5), ('bob', 17), ('barb', 5)]
def tableOfAvgScores(list):
    print("Person", "Average Score")
    clist = list[:]

    previous_name = clist[0][0]
    idx = 0
    name = 0
    score = 1
    #for current in clist:
       # if current[idx][name] ==

# Visualizing Frequency Distribution
data = [3,3,5,7,1,2,5,2,3,4,6,3,4,6,3,4,5,6,6]
import turtle
def frequencyChart(alist):
    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1

    itemlist = list(countdict.keys())
    minitem = 0
    maxitem = len(itemlist) - 1

    countlist = countdict.values()
    maxcount = max(countlist)

    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1,-1,maxitem+1, maxcount+1)
    chartT.hideturtle()

    chartT.up()
    chartT.goto(0,0)
    chartT.down()
    chartT.goto(maxitem, 0)
    chartT.up()

    chartT.goto(-1,0)
    chartT.write("0", font=("Helvetica", 16, "bold"))
    chartT.goto(-1, maxcount)
    chartT.write(str(maxcount), font=("Helvetica", 16, "bold"))

    itemlist.sort()

    for index in range(len(itemlist)):
        chartT.goto(index, -1)
        chartT.write(str(itemlist[index]), font=("Helvetica", 16, "bold"))

        chartT.goto(index,0)
        chartT.down()
        chartT.goto(index, countdict[itemlist[index]])
        chartT.up()



    wn.exitonclick()

frequencyChart(data)
# STANDARD DEVIATION
# Listing 4.11 pg 150
import math

def standardDev(alist):
    theMean = mean(alist)

    total = 0
    for item in alist:
        difference = item - theMean
        diffsq = difference ** 2
        total += diffsq

    sdev = math.sqrt(total/(len(alist)-1))
    return sdev

b_list = [7,11,9,18,15,12]
#print(standardDev(b_list))









