#Archimedes approximation of pi

import math

def archimedes_pi(n):
    """Approximate Pi by considering the perimeter of regular polygons,
    inscribed in a unit circle"""

    return n * math.sin(math.radians(360/(2*n)))

#Build functions
#1 area if a circle
def area_circle(radius):
    pi = math.pi
    area = pi * (radius * radius)
    print(area)

#area_circle(5)

#2 circumference of a circle
def circumference_circle(radius):
    pi = math.pi
    circum = 2 * pi * radius
    print(circum)

#circumference_circle(5)

#3 volume of sphere
def volume_sphere(radius):
    r = radius * radius * radius
    pi = math.pi
    volume = 4 / 3 * pi * r
    print(volume)

#volume_sphere(5)

#4
#print(16 * math.atan(1/5) - 4 * math.atan(1/239) )

#print((math.log((640320*640320*640320)+ 744))/ math.sqrt(163))

# Accumulators
# Example 1: sum of numbers 1 - 5
acc = 0
for x in range(1,6):
    acc += x

#print(acc)

# Example 2: sum of numbers 1 - 100
acc = 0
for x in range(2, 101, 2):
    acc += x

#print(acc)

# Example 3: factorial
acc = 1
n = 10
for x in range(1, n+1):
    acc *= x

#print(acc)

# Example 4: Fibonacci Sequence

def fibonacci(n):
    fib1 = 1
    fib2 = 1
    fibN = 0
    for i in range(2, n):
        fibN = fib1 + fib2
        fib1 = fib2
        fib2 = fibN

    return fibN

#print(fibonacci(6))


# Leibniz approximation of Pi
# for 6 terms: range(1, 12, 4) = {1, 5, 9}

def leibniz_pi(number_of_terms):
    pie = 0
    #p1 = 0
    #p2 = 0
    for i in range(1, 2* number_of_terms, 4):
        pie += 4/i
        #p1 += 4/i

    for i in range(3, 2* number_of_terms, 4):
        pie -= 4/i
        #p2 += 4/i

    #pie = p1-p2
    return pie

#print(leibniz_pi(500))




# CAME BACK TO ON 02/01/2018
#Wallis formula of Pi
def wallis_pi(n):
    pie = 1

    for i in range(1, n+1):
        exp1 = (2 * i) / ((2 * i) - 1)
        exp2 = (2* i) / ((2 * i) + 1)
        pie *= exp1 * exp2
    return 2 * pie

print(math.pi - wallis_pi(1000))
print(math.pi - archimedes_pi(1000))
print(math.pi - leibniz_pi(1000))
print(math.pi)

n = 10000
for i in range(1000, n + 1):
    a_pie = archimedes_pi(i)
    l_pie = leibniz_pi(i)
    w_pie = wallis_pi(i)
    #print("Archimedes: " + str(abs(a_pie-math.pi)))
    #print("Leibniz: " + str(abs(l_pie - math.pi)))
    #print("Wallis: " + str(abs(w_pie - math.pi)))












