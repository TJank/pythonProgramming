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
print("-"*20)
rand_list = randomList_gamma(1000, 2, 2)
print(rand_list)

points = rand_list
bins = int(np.max(rand_list) - np.min(rand_list))
print(bins)
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
    if not len(list) % 2 == 0:
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
points = [(1,2),(5,1),(-1,5),(-5,7),(-8,-2),(-4,-1),(2,-10),(8,-3),(4,-8),(5,5)]

def plotRegression(points):


# Problem 5.
#def gcd(x, y):
    x1 = abs(min(x, y))
    y1 = abs(max(x, y))
    gcd_ = x1

    if y1 % x1:
        gcd_ = gcd(x1, y1 % x1)
    return gcd_

#print(gcd(2,100))

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

# Problem 9.






















