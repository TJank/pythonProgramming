# Question 1
#part 1
part1 = 0
for i in range(0,101,2):
    part1 += i
print(part1)

# part 2
part2 = 0
for i in range(1,101):
    part2 += i ** 2
print(part2)

# part 3
acc = 1
for i in range(0,21):
    acc *= 2 ** i
    #print(i)
print(acc)

# part 4
part4 = 1
#a = int(input("Please input a number."))
#b = int(input("Please input a second number."))
#for i in range(a,b + 1,1):
    #if not i % 2 == 0:
        #part4 *= i
        #print(i)

#print(part4)

#part 5
part5 = 0
input1 = input("Please enter 5 or more numbers.")
for num in input1:
    if not int(num) % 2 == 0:
        part5 += int(num)
print(part5)

# Question 2

# Question 3
a = 32310901
b = 1729
m = 2**24
rold = int(input("Please pick a number."))
for i in range(100):
    rnew = (a * rold + b) % m
    print(rnew)
    rold = rnew

# Question 4

# Question 5














