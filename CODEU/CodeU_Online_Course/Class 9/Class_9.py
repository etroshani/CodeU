#Welcome to your 9th CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own.


## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


#   In this class, we are covering these topics:
#       - Introduction to the Turtle Module
#       - Turtle Exercisees



####    FIRST PART    ####

##     Introduction to the TURTLE Module     ##

# Explain the utility of the Turtle Module and how it is used!

# We must always start our TURTLE programs with import turtle 
# and finish the code with turtle.done() so that the window remains open
import turtle

# Initiate a Turtle pen
pen = turtle.Turtle()


##  Properties of the Turtle pen  ##

# Color
pen.color("blue")
#pen.color("#000000")     # Explain what is a HEX (#000000) value of a color and how to find it!

# Pen Size
pen.pensize(10)

# Pen Shape
pen.shape("turtle")
pen.shape("square")

# Pen Speed: This allows use to determine the speed that the pen will draw!
pen.speed(1)


##  Pen Manipulations  ##

# Pen Movements
"""
pen.forward()
pen.backward()
"""

# Pen Rotations
"""
pen.left()
pen.right()
"""

#Go To and Set Position functions: This allows us to move the pen around to specific coordinates!
"""
pen2.setpos(0, 200)
pen2.goto(200,200)
"""

# Pen up and Pen down functions: This allows us to move the pen on our canvas without drawing!
"""
pen.forward(100)
pen.penup()
pen.forward(100)
pen.pendown()
pen.forward(100)
"""

# Multiple pens on the same canvas
"""
pen2 = turtle.Turtle()
pen2.color("green")
pen2.pensize(10)
"""



####    SECOND PART    ####

##   Exercise 1: Draw a square!   ##
"""
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
"""

##   Exercise 2: Draw a circle!   ##
"""
pen2.penup()
pen2.backward(200)
pen2.pendown()
pen2.circle(40)
"""

# Fill and End Fill: This allows us to fill the shapes we draw with color!
"""
pen2.color("green","yellow")    # The first color("green") is the color of the pen. The second("yellow") is the color of the fill!
pen2.begin_fill()               
pen2.circle(40)
pen2.end_fill()
"""

###    Final Exercise Of The Day: Build Traffic Lights!    ###

## 1) Create Pens ##
"""
red = turtle.Turtle()
red.color("black","red")

yellow = turtle.Turtle()
yellow.color("black", "yellow")

green = turtle.Turtle()
green.color("black", "green")
"""

## 2) Start Drawing ##
#--Red Light--#
"""
red.begin_fill()
red.circle(20)
red.end_fill()
"""

#--Yellow Light--#
# Set the position for the yellow pen
"""
yellow.penup()
yellow.setpos(0,-40)
yellow.pendown()
"""

# Draw
"""
yellow.begin_fill()
yellow.circle(20)
yellow.end_fill()
"""

#--Green Light--#
# Set the position for the green pen
"""
green.penup()
green.setpos(0,-80)
green.pendown()
"""

# Draw
"""
green.begin_fill()
green.circle(20)
green.end_fill()
"""



####    HOMEWORK: Olympic Rings!    ####

#   The commissioner of the Olympics has asked you to create the Olympic rings using Python!
#   The Olympic rings contain 5 rings of different colors: Blue, Black, Red, Green, and Yellow
#   1) Each ring has a radius of 50
#   2) The distance between each ring is 80

#   STEPS:
#       1) Create 2 pens for the first and second row of rings
#       2) Set the position for the first ring on the first row
#       3) Draw all 3 rings of the first wor
#       4) Set the position for the first ring on the second row
#       5) Draw the last rings


####    HOMEWORK CORRECTION    ####

# Create 2 separate pens for the 2 rows or rings
"""
p1 = turtle.Turtle()
p2 = turtle.Turtle()
"""

## First Row Of Rings##
# 1) First Ring: Blue
# Set the position for the first ring
"""
p1.penup()
p1.setpos(-80, 80)
p1.pendown()
"""

# Draw the ring
"""
p1.color("blue")
p1.circle(50)
"""

# 2) Second Ring: Black
# Set the position for the second ring
"""
p1.penup()
p1.forward(80)
p1.pendown()
"""

# Draw the ring
"""
p1.color("black")
p1.circle(50)
"""

# 3) Third Ring: Red
# Set the position for the third ring
"""
p1.penup()
p1.forward(80)
p1.pendown()
"""

# Draw the ring
"""
p1.color("red")
p1.circle(50)
"""

## Second Row Of Rings ##
# 1) Fourth Ring: Green
# Set the position for the first ring
"""
p2.penup()
p2.setpos(-40, 0)
p2.pendown()
"""

# Draw the ring
"""
p2.color("green")
p2.circle(50)
"""

# 2) Fifth Ring
# Set the position for the fifth ring
"""
p2.penup()
p2.forward(80)
p2.pendown()
"""

# We can now draw our final circle!!!
"""
p2.color("yellow")
p2.circle(50)
"""

turtle.done()