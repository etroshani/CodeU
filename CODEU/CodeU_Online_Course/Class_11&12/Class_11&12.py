#Welcome to your 11th and 12th CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own.


## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


#   In these classes, we are covering:
#       - Final CodeU Project: TURTLE RACE



####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       - Efficient ways to draw shapes
#       - Complex Turtle Exercises


##   REVIEW HOMEWORK   ##
# Review the homework to correct any mistake they may have done or to answer any question they may have.




####    SECOND PART    ####


####        Final CodeU Project: TURTLE RACE        ####

# Import the necessary modules for this project
import turtle
import random
import time

## Screen Background ##
turtle.bgcolor("#00ff85")       # Another color option could be: #00a556
turtle.color("white")
turtle.speed(0)                 # This allows us to directly draw
turtle.penup()
turtle.goto(-220,240)
turtle.write("CODEU TURTLE RACE", font=("Helvetica", 40, "bold"))


## Finish Line ##

turtle.color("white")
turtle.shape("square")
turtle.shapesize(0.75)
turtle.penup()

squareSize = 15

# First vertical line of squares
for i in range(9):
    turtle.setpos(250, 150 - (i*squareSize*2))
    turtle.stamp()

# Second vertical line of squares
for i in range(9):
    turtle.setpos(250+squareSize, (150-squareSize) - (i*squareSize*2))
    turtle.stamp()


## Our Turtles ##

# 1st Turtle
t1 = turtle.Turtle()
t1.speed(0)
t1.color("blue")
t1.shape("turtle")
t1.penup()
t1.goto(-250,100)
t1.pendown()

# 2nd Turtle
t2 = turtle.Turtle()
t2.speed(0)
t2.color("yellow")
t2.shape("turtle")
t2.penup()
t2.goto(-250,50)
t2.pendown()

# 3rd Turtle 
t3 = turtle.Turtle()
t3.speed(0)
t3.color("purple")
t3.shape("turtle")
t3.penup()
t3.goto(-250,0)
t3.pendown()

# 4th Turtle 
t4 = turtle.Turtle()
t4.speed(0)
t4.color("black")
t4.shape("turtle")
t4.penup()
t4.goto(-250,-50)
t4.pendown()

# Set a slight delay before the race starts
time.sleep(1) 

## Turtle Movement ##

# Create a while loop that will keep looping until a turtle has reached a specific position, the finish line.
while True:    

    # The turtle are able to move forward by 1 to 5 pixels determined randomly
    t1.forward(random.randint(1,5))
    t2.forward(random.randint(1,5))
    t3.forward(random.randint(1,5))
    t4.forward(random.randint(1,5))
    
    # Set the conditionals where if a turtle reaches the finish line(x>=240) or further, the turtle wins and the loop is broken.
    if t1.pos() >= (240,100):
        turtle.setpos(-220,-240)
        turtle.write("The blue turtle has won!!", font=("Helvetica", 40, "bold"))
        turtle.hideturtle()
        break
    elif t2.pos() >= (240,50):
        turtle.setpos(-220,-240)
        turtle.write("The yellow turtle has won!!", font=("Helvetica", 40, "bold"))
        turtle.hideturtle()
        break
    elif t3.pos() >= (240,0):
        turtle.setpos(-220,-240)
        turtle.write("The purple turtle has won!!", font=("Helvetica", 40, "bold"))
        turtle.hideturtle()
        break
    elif t4.pos() >= (240,50):
        turtle.setpos(-220,-240)
        turtle.write("The black turtle has won!!", font=("Helvetica", 40, "bold"))
        turtle.hideturtle()
        break

turtle.done()