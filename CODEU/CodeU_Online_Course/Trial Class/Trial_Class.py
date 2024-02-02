
####        WELCOME TO THE DEMO CLASS       ####

#your first code!

print("Hello World!")

####   Introduction to Comments:    #### 
#   If a # is added before a code, it will be ignored when the code is executed. This is used to add descriptions to your code.

#this comment will be ignored


####   TASK 1: python as a calculator   ####
#additions and substractions
print(5+5)
print(5-5)
print("5+5") 

#multiplications
print(5*2)
print("apple"*3) 
print("apple*3") 

#divisions
print(10/2)
#print("apple"/2) #This will show an error since a String('apple') cannot be divided by an Integer(2) 


####   TASK 2: Python as a drawing pad using TURTLE module  ####

#import TURTLE -->  TURTLE is a module designed to showcase your code in a more interactive and visual way. This was created
#                   for younger coders to visualize their code. It allows you to draw on a drawing pad using code as directions.



####    Your first drawing: The OLYMPIC RINGS!  ####

#   1) import module - We need to import our module to be able to use it in our code
import turtle  

#   2) Create a turtle pen. This will allow use to give it commands and directions. Here we are calling it 'pencil'.
#      You can name whatever you like.
pencil = turtle.Turtle()

#   3) Let's move our turtle.
pencil.forward(50) 

#   4) We can change the pen size.
pencil.pensize(6)

#   5) Let's set a starting point. We use penup() to remove our pen from the drawing boad to be able to move it to a different
#      location without it drawing. We then use pendown() to place it back on the board so can start drawing again.
pencil.penup()
pencil.goto(-200, 100)
pencil.pendown()

#   6) Let's draw our first circle with the function .cricle()! The number inside the parentheses () will be the size. 
#      Here the size is 50. We also assign the color BLUE to our circle.
pencil.color("blue")
pencil.circle(50)

#   7) Once the circle is drawn, let's move to a different location.
pencil.penup()
pencil.forward(110)
pencil.pendown()

#   8) We can now draw a second circle! Here we assign the color black to our circle.
pencil.color("black")
pencil.circle(50)

#   9) Let's make the pen move once again. Don't forget to use penup() and pendown() whenever you need to move the pen without
#      it drawing on the board.
pencil.penup()
pencil.forward(110)
pencil.pendown()

#   10) Go ahead and draw a third circle
pencil.color("red")
pencil.circle(50)

#   11) Let's move to the fourth circle. Here, we have to rotate the pen for it to go in the direction we want. 
pencil.penup()
pencil.left(180)        # This turns the pen perfectly to the opposite side(behind it).
pencil.forward(55)
pencil.right(90)        # This turns the pen perfectly to the right of it.
pencil.forward(50)
pencil.left(90)         # This turns the pen perfectly to the left of it.
pencil.pendown()

#   12) We can now draw our fourth circle
pencil.color("green")
pencil.circle(50)

#   13) Let's move the pen for our last circle
pencil.penup()
pencil.forward(110)
pencil.pendown()

#   14) We can now draw our final circle!!!
pencil.color("yellow")
pencil.circle(50)