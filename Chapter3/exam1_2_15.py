# Code for Exam 1
import random
import turtle
import math

# Problem 1. Making 10 digit number more readable
def phoneNumber():
    numbers = input("Please enter your 10 digit phone number.")
    areaCode = numbers[:3]
    first3 = numbers[3:6]
    last4 = numbers[6:]
    if len(numbers) != 10:
        print("Error: THe number must contain exactly 10 digits.")
    else:
        print("(" + areaCode + ")" + " " + first3 + "-" + last4)

#phoneNumber()


# Problem 2. Emulating flip of two coins
def coinFlip():
    input("Call it in the air: Heads or Tails?")
    computersPick = random.randrange(0,2)
    if computersPick == 0:
        print("It landed on heads.")
    elif computersPick == 1:
        print("It landed on tails.")
    else:
        print("Did you call it?")

#coinFlip()

# Problem 3. Palindromes
word = "racecar"

def palindromeTest(word):
    backwards = ""
    wordLen = len(word)
    for index in range(0,len(word)):
        backwards = backwards + word[(len(word)-1)-index]

    if backwards == word:
        return True
    else:
        return False


#print(palindromeTest(word))


# Problem 4. draw flower with squares
# define draw square
def draw_square(a_turtle, sidelength):
    for i in range(4):
        a_turtle.forward(sidelength)
        a_turtle.right(90)

bill = turtle.Turtle()


def draw_flower(a_turtle, n, sidelength, color):
    bill.pencolor(color)
    for i in range(n):
        draw_square(a_turtle, sidelength)
        bill.right(360/n)

draw_flower(bill, 21, 200, "yellow")
turtle.done()
# CANT FILL

# Problem 5
# a.
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
#print(grade(77))

# b.
def draw_square2(a_turtle, sidelength):
    for i in range(4):
        a_turtle.forward(sidelength)
        a_turtle.right(90)

# c. TRUE
# d. TRUE
# e. TRUE

# f.
def draw_triangle(a_turtle, side_length):
    for i in range(3):
        a_turtle.forward(side_length)
        a_turtle.left(120)

# g.
def rollDice():
    sideUpp = random.randrange(1,7)
    if sideUpp == 1:
        print("You rolled a 1")
    elif sideUpp == 2:
        print("You rolled a 2.")
    elif sideUpp == 3:
        print("You rolled a 3.")
    elif sideUpp == 4:
        print("You rolled a 4.")
    elif sideUpp == 5:
        print("You rolled a 5.")
    elif sideUpp == 6:
        print("You rolled a 6.")



