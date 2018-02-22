# List - mutable ordered collection of objects
import math

a_list = [1, 3.5, 6, 2, math.pi]
print(a_list[-1])
print(a_list[2:4])

b_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b_list = []
for i in range(10):
    b_list.append(i)

print(b_list)


a_list = b_list
a_list.append(10)
print(b_list)
print(a_list)

b_list = "Hello World"

print(a_list)
print(b_list)

c_word = b_list + "."

d_list = a_list.append(11)
print(a_list)
print(d_list)

d_list = a_list

d_list[3] = "cat"
print(a_list)




# List Functions:

# List of all numbers from 1-100
print("-"*40)

L = []
for i in range(1,101):
    L.append(i)

print(L)


# Add elements to L
# append: add an element to the END of the list

L.append(101)
print(L)

# Insert: adds an element into a given index

L.insert(5, "obvious")
print(L)

# replace: change the value at some index

L[5] = "less obvious"
print(L)

# L.clear()

L.pop(5)
print(L)

# L.pop()
# L.remove()

# List Comprehensions: syntactic simplification of construction of lists

# List of numbers from 1 to 10
x = [i for i in range(1,11)]

y = [2*i for i in range(1,11)]

print(x)
print(y)


z = [i for i in range(1,11) if i % 2 == 0]
print(z)


# First 100 even numbers
ex = [i for i in range(1,201) if i % 2 == 0]
print(ex)
print(len(ex))

# List of the following numbers in sequence: 4, 6, 8, 10, 12
q = [2*i + 2 for i in range(1,6)]
print(q)

# List of the following numbers in sequence: 1, 4, 22,
L = []
x = 1
for i in range(5):
    L.append(x)
    x = 2 * x + 2

print(L)



ages = [21, 21, 20, 21, 19, 21, 21, 8, 41, 45, 32, 56]

# Mean: average value of the collection
def mean(data):
    total = 0
    for i in data:
        total += i

    return total/len(data)

def mean1(data):
    total = 0
    for i in range(len(data)):
        total += data[i]

    return total/len(data)

print(mean(ages))


# Median, Mode, Standard Deviation























