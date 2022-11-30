#Welcome to your 9th CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own.


## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


#   In the 10th class, we are covering these topics:
#       - Efficient ways to draw shapes
#       - Complex Turtle Exercises



####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       - Introduction to the Turtle Module
#       - Turtle Exercises


##   REVIEW HOMEWORK   ##
# Review the homework to correct any mistake they may have done or to answer any question they may have.



####    SECOND PART    ####

##     Drawing shapes efficiently using Loops!    ##
import turtle

# Create your pen
p1 = turtle.Turtle()
p1.color("blue")
p1.pensize(10)
p1.shape("turtle")

# Triangle
for i in range(3):
    p1.forward(100)
    p1.left(120)

# Square
for i in range(4): 
    p1.forward(100)
    p1.left(90)

# Hexagon
for i in range(6):
    p1.forward(100)
    p1.left(60)

# Star
p1.color("yellow", "green")
p1.begin_fill()
for i in range(8):
    p1.forward(100)
    p1.left(135)
p1.end_fill()


##     Exercise 1: Choose your shape!     ##
print("You can choose to draw a variety of shapes with different colors!") 
print("\nHere are your choices of shapes: circle | triangle | square | rectangle | rectangle | star")
print("\nHere are your choices of colors: blue | green | yellow | red | pink | purple | brown | beige")
print("\nYou can choose a color for the outline of your shape, and a different color for the inside!")

# Set your conditionals
while True:
    shape = input("\nChoice of shape: ")
    outline = input("Choice of outline color: ")
    inside = input("Choice of inside color: ")

    p1.color(str(outline), str(inside))

    p1.clear()

    if shape == "circle":
        p1.begin_fill()
        p1.circle(50)
        p1.end_fill()

    elif shape == "triangle":
        p1.begin_fill()
        for i in range(3):
            p1.forward(100)
            p1.left(120)
        p1.end_fill()

    elif shape == "square":
        p1.begin_fill()
        for i in range(4): 
            p1.forward(100)
            p1.left(90)
        p1.end_fill()

    elif shape == "rectangle":
        p1.begin_fill()
        for i in range(2):
            p1.forward(100)
            p1.left(90)
            p1.forward(30)
            p1.left(90)
        p1.end_fill()
        
    elif shape == "hexagon":
        p1.begin_fill()
        for i in range(6):
            p1.forward(100)
            p1.left(60)
        p1.end_fill()

    elif shape == "star":
        p1.begin_fill()
        for i in range(8):
            p1.forward(100)
            p1.left(135)
        p1.end_fill()
    
    answer = input("Do you want to keep playing? yes or no: ")
    
    if answer == "no"
        print("Thanks for playing!")
        break
    else:
        continue


##     Final Exercise Of The Day: Abstract Art!     ##
import random

p1.speed(5)

for i in range(10):
    # Set your colors
    listColors = ["green", "yellow", "blue", "red", "cyan", "orange", "pink", "black", "purple"]
    randomColor = random.randrange(0,len(listColors))
    randomFillColor = random.randrange(0,len(listColors))
    p1.color(listColors[randomColor], listColors[randomFillColor])
    
    # Set your positions
    positionx = random.randrange(-250,250)
    positiony = random.randrange(-250,250)
    p1.penup()
    p1.goto(positionx,positiony)
    p1.pendown()

    # Draw your circle
    p1.begin_fill()
    p1.circle(random.randrange(10,80))
    p1.end_fill()



####    HOMEWORK: Build your house!    ####

#   The mayor of your town has asked you to draw a sketch of a house to determine what types of houses he should build in the city!
#   The house can be of any shape or form, be any color, and be any size. However, there are requirements.
#   Requirements:
#   1) The house must have a ROOF(triangular, etc.)
#   2) The house must have a DOOR(rectangle, circle, etc.)
#   3) The house must have AT LEAST 1 WINDOW(circle, square, etc.)

#   STEPS:
#       1) Create your pen
#       2) Set a an outline color and a fill color for each element of your drawing (Ex.: Door)
#       3) Set a starting position when drawing an element
#       4) Draw the element in the MOST efficient way


####    HOMEWORK CORRECTION    ####

##  Create your pen  ##
h1 = turtle.Turtle()
h1.pensize(6)

##  House  ##
# Color
h1.color("black", "orange")

# Position
h1.penup()
h1.goto(-100,-100)
h1.pendown()

# Square House
h1.begin_fill()
for i in range(4):
    h1.forward(200)
    h1.left(90)
h1.end_fill()

##  ROOF  ##
# Color
h1.color("#573f2b", "firebrick")

# Position
h1.penup()
h1.goto(-112,80)
h1.pendown()

# Triangle Roof
h1.begin_fill()
for i in range(3):
    h1.forward(225)
    h1.left(120)
h1.end_fill()


##  WINDOW  ##
# Color
h1.color("black", "beige")

# Position
h1.penup()
h1.goto(20,0)
h1.pendown()

# Square Window
h1.begin_fill()
for i in range(4):
    h1.forward(55)
    h1.left(90)
h1.end_fill()


##  WINDOW CROSS  ## (OPTIONAL)
# Position
h1.penup()
h1.goto(20,27.5)
h1.pendown()

# First line
h1.forward(50)

# Position 2nd Line
h1.penup()
h1.goto(47.5,0)
h1.pendown()
h1.left(90)

# 2nd Line
h1.forward(50)


##  DOOR  ##
# Color
h1.color("black","brown")

# Position
h1.right(90)
h1.penup()
h1.goto(-60,-100)
h1.pendown()

# Rectangle Door
h1.begin_fill()
for i in range(2):
    h1.forward(50)
    h1.left(90)
    h1.forward(100)
    h1.left(90)
h1.end_fill()


turtle.done()