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




















