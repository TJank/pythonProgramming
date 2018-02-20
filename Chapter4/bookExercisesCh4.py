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
print(range(10))
print(list(range(10)))
print(list(range(10,2,-2)))
print(list("the quick fox"))

# Session 4.6 LIST METHODS pg 126
myList = [1024,3,True, 6.5]
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
myList.pop()
print(myList)
myList.pop(1)
print(myList)
print(myList.pop(2))
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)

# Session 4.7 pg 127
a = "minnesota vikings"
print(a.split())
print(a.split('i'))
print(a.split('nn'))

# Exercises PG 127
# 4.1
list = [7,9,'a','cat',False]
list.append(3.14)
list.append(7)
print(list)
list.insert(3,'dog')
print(list.index('cat'))
count = list.count(7)
print(count)
list.remove(7)
print(list)
list.pop(2)
print(list)

# 4.3
string = "the quick brown fox"
listOfWords = []
listOfWords.append(string[0:3])
listOfWords.append(string[4:9])
listOfWords.append(string[10:15])
#print(listOfWords)

mylist410 = [1,4,(1,2,3),10]

print(mylist410)

# Session 4.8 pg 129
alist = [20,32,21,26,33,22,18]
print(max(alist))
print(min(alist))
print(max('house'))
print(min('house'))
print(max(alist)- min(alist))

# listing 4.1 pg 130
def getRange(alist):
    return max(alist) - min(alist)

# Session 4.9
print(getRange([2,4]))
print(getRange(alist))

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











