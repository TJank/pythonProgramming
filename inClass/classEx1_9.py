# Code goes here
jeffrey = 2 + 3
Jeffrey = 2 + 3

x = "Hello World!"

my_word = "Hello World!"

print(jeffrey)
print(x)

JEFFREY = jeffrey + Jeffrey
print(JEFFREY)

# y = jeffrey + x
z = jeffrey * x
print(z)


# exercise 1:  add 8 + 9 + 10 and print out the result
print("8 + 9 + 10 =" + str(8 + 9 + 10))

# exercise 2:  Print the number of inches in x miles
miles = 500
feet = 5280
inches = 12
print("Number of inches in " + str(miles) + " miles is " + str(miles*feet*inches))


# exercise 3: Calculate and print the average age of all the people in your table
age1 = 18
age2 = 20
age3 = 22
print("The average age is =" + str((age1 + age2 + age3)/3))


# Integer division and residue
x = 24
y = 13
print(x // y)  # integer division
print(x % y)   # residue from integer division


# Find the number of handshakes of if all people in your table shook hands
print()
number_of_people = 60
print("The number of handshakes between " + str(number_of_people) + " people is " + \
      str((number_of_people - 1) * number_of_people // 2))


# Iterators and accumulators
# we use iterators to repeat certain steps
# we use accumulators to "accumulate" quantities

x = 0
for i in range(60):
    x += i

print(x)


# Multiply all numbers from 1-100

x = 1
for i in range(1, 101):
    x *= i

print(x)


# Factorial
number = 10
fact = 1
for i in range(1, number + 1):
    fact *= i

print(fact)

# Functions
# and abstraction of a procedure
def factorial(n):
    if n == 0:
        return 1
    else:
        f = 1
        for j in range(1, n / 1):
            f *= j
        return f

print(factorial(5))

# Calculate the factorial of 1000
f = factorial(5)
x = print(f)
print(x)