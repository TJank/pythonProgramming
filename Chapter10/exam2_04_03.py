# EXAM 2 GOOD LUCK LOL xD
# name: Tyler Jankowski
import math

# Part 1 Questoin 2:

def cosSim(x,y):
    xsum = 0
    ysum = 0
    xysum = 0

    for i in range(len(x)):
        _x = x[i]
        _y = y[i]
        xsum += _x * _x
        ysum += _y * _y
        xysum += _x * _y
    return xysum / math.sqrt(xsum * ysum)

x = [3, 45, 7, 2]
y = [2, 54, 13, 15]
print(cosSim(x,y))

# Part 2 Question 7:

def list_shitf(a_list, num_shifts, direction):
    rotate_list = []
    if direction == "R":
        for i in range(num_shifts):
            popped = a_list.pop()
            a_list.insert(0,popped)
            #print(a_list)

    if direction == "L":
        for i in range(num_shifts):
            popped = a_list.pop(0)
            a_list.append(popped)
            #print(a_list)

    return a_list


test_list = [3,6,7,8,4,5,2]
print(list_shitf(test_list,3,"L"))

# Part 2 Question 5

def listOf7s():
    divisible_by_7 = []
    for i in range(1000000,9999999,1):

        if i % 7 == 0:
            #print(i)
            divisible_by_7.append(i)
            #print("DIVISIBLE BY 7")

    print(len(divisible_by_7))
    return divisible_by_7

listOf7s()


# EXTRA CREDIT QUESTION 3:

def row_multiply(a_matrix, row_num, constant):

    for i in range(len(a_matrix[row_num])):
        a_matrix[row_num][i] = a_matrix[row_num][i] * constant

    return a_matrix





matrix1 = [[1,5,9,3],
           [3,7,6,2],
           [4,2,8,5]]

print(row_multiply(matrix1,0,2))



