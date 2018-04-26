import turtle
import math
import random
import os
import winsound

# Modify the Asteroids game so that the game ends after the playes loses 3 lives. Create a lives counter,
# and substract a life every time the players touches a boundary


# Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("bgpic.gif")
wn.tracer(3)

# Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
# mypen can be reused... will be used to draw score on the screen


# Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)

# Create the score variable
score = 0

# Create goals
maxGoals = 10
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
    goals[count].right(random.randint(0, 360))

# Set speed variable
speed = 1

# Define functions
def turnleft():
    player.left(30)


def turnright():
    player.right(30)


def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    if speed > 1:
        speed -= 1


def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

# Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

lives = 3

#while True:
while lives > 0:
    player.forward(speed)

    # Boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.goto(0, 0)
        player.right(180)
        lives -= 1
        scorestring = "Score: {0}     Speed: {1}     Lives: {2}".format(score, speed, lives)
        mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        #os.system("afplay bounce.mp3&")
        #winsound.PlaySound("omxplayer bounce.mp3")

    # Boundary Checking
    if player.ycor() > 300 or player.ycor() < -300:
        player.goto(0, 0)
        player.right(180)
        lives -= 1
        scorestring = "Score: {0}     Speed: {1}     Lives: {2}".format(score, speed, lives)
        mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        #os.system("afplay bounce.mp3&")
        #winsound.PlaySound("bounce.mp3", winsound.SND_FILENAME)

    # Move the goal
    for count in range(maxGoals):
        goals[count].forward(3)

        # Boundary Checking
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
            #os.system("afplay bounce.mp3&")

            # Boundary Checking
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
            #os.system("afplay bounce.mp3&")

            # Collision checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0, 360))
            #os.system("afplay collision.mp3&")
            score +=1
            #lives -= 1
            # Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: {0}     Speed: {1}     Lives: {2}".format(score, speed, lives)
            mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))



#delay = input("Press Enter to finish.")