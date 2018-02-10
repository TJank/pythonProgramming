import random
import math
import turtle

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




def showMontePi(numDarts):
    wn = turtle.Screen()
    drawingT = turtle.Turtle()

    wn.setworldcoordinates(-2,-2,2, 2)

    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)

    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)

    circle = 0
    drawingT.up()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        d = math.sqrt(x**2 + y**2)

        drawingT.goto(x,y)

        if d <= 1:
            circle = circle + 1
            drawingT.color("blue")
        else:
            drawingT.color("red")

        drawingT.dot()

    pie = circle / numDarts * 4

    wn.exitonclick()
    print(pie)
    return pie

#showMontePi(1000)



# Doesnt WORK :( ????
def montecarlo_pi(num_darts):
    hits = 0
    for i in range (100):
        x = 2 * random.random() - 1
        y = 2 * random.random() - 1

        if(math.sqrt(x**2 + y**2) < 1):
            hits += 1

    pie = 4 * hits / num_darts
    return pie

#print(montecarlo_pi(1000))

# Compound interest A = p(1 + (r/n)^nt
# A = future value
# P = Principal
# r = annual interest rate (as decimal)
# n = number of times a year
# t = number of years

def compoundInt(p, r, n, t):
    A = (p * (1 + (r/n))**(n*t))
    return A

#print(compoundInt(1000, .10, 12, 10))
