#Welcome to your 1st CODEU class!

#   This is just a guide, try to incorporate your knowledge into your teaching. Make sure you adjust to the student's speed.
#   If you know a more efficient way to code one of the exercises, feel free to change it, as long as the end result is the same!
#   In the end, you are the tutor so don't limit yourself with this guide!

#   DON'T FORGET TO EXPLAIN THE REASONING BEHIND EACH CODE, UNDERSTANDING THE MATERIAL IS VERY IMPORTANT!!
#   You are teaching a beginner, so make sure they are able to recreate the code on their own


####    FIRST PART    ####
 
# Introduction: Getting to know the student (their name, age, interests, reason they want to code)

# Follow the PowerPoint 

# Explain VSC features (New folder, New File, New window, Save as, Run a program, Debug, etc.)

# Explain very briefly the history and utility of coding 
#    (e.g.: how coding is the basis of all applications, websites and software)



## ***Once they are comfortable with a concept, ask them to create an example to see if they properly understood*** ##


##   1. Your first code!    ##

#   Code 'Hello World' and other possible Strings using print(). Explain what a STRING is!
print("Hello World")

#   Defining a variable
x = "Hello World"
print(x)

#   Overriding a variable
x = "Hello"
x = "I'm hungry!"
print(x)

#   Combining Strings
x = "My name is Francis"
y = " I am 50 years old"
z = " and I like fruits!"
print(x + "," + y + z)


##   2. Turning Python into a Calculator!   ##

#   Resolve mathematical formulas using int and float.


#   Additions

# Example 1
print(5+5)

# Example 2
x = 2
print(x + 3)

# Example 3
x = 1
x = x+1
print(x)

# More efficient way to add to variable x
x = 1
x += 1
print(x)

# Example 4
x = 2
y = 3
print(x+y)


#   Substractions

# Example 5
x = "20"
y = "60"
print(y-x)

# Example 6
x = 0.25
y = 0.15
print(x-y)

# Example 7
x = 25
y = 15
z = x - y
print(z)


#   Multiplications

# Example 8
x = 3
y = 4
z = x*y
print(z)

# Example 9
x = -5
y = 6
print(x-y*5)
print((x-y)*5)


#   Modulo
x = 10
y = 3
print(x % y)

#   Floor division
x = 10
y = 3
print(x // y)

#   Rounding
round(4.5)


##  3. Introduction to Operators, Arithmetic Operations, and Booleans  ## 
# This will be very useful in something called CONDITIONALS and LOOPS. We will cover this in future projects and exercises!
x = 5 == 6          #Explain meaning of ==
print(x)
x = 5 < 6           #Explain meaning of <
print(x)
x = 5 <= 6          #Explain meaning of <=
print(x)
x = 5 != 6          #Explain meaning of !=
print(x)


#   Introduction to AND, OR and NOT statements. Explain their functionnalies and why they will be very useful in conditionals.

# And
x = 10
print( x < 15 and x > 5)

# OR
x = 10
print( x > 15 or x < 100)

# NOT
x = 10
print(not x < 20) 



####    SECOND PART    ####

#   In the second part, we'll learn how to use INPUT. This will be the first interactive code the student(s) will make!
#   They'll learn how to use INPUT with strings, integers and floats. At the end, they'll code a small exercise where
#   they have to create a list of guests!


##  4. Strings, Integers, Floats and Booleans  ##

# Explain what Strings, Integers, Floats and Booleans are. Give Examples!
strings = "A string is a sequence of characters that is read as ONE element. It can be letters, numbers, symbols, and emojis"

integers = 5    # An Integer(int) is a value used to represent real numbers that DO NOT HAVE decimals("numbers after the comma").

floats = 5.55   # A Float(float) is a value used to represent real numbers that HAVE decimals("numbers after the comma").

Booleans = True    # Boolean statements are statements that evaluate to be true or false.
Booleans = False   # This is often used in functions and conditionals.


#### 5. Introduction to INPUT! ####

# Example 1: Welcome to the world of coding!
name = input("What is your name?: ")
print(name)
print("Welcome "+ name + " to the world of coding!")

# Example 2: Let's calculate something!
x = input("First number: ")
y = input("Second number: ")
product = int(x)*int(y)
print(product)




###     HOMEWORK   |    Creating an interactive calculator! ###

# Create a calculator that can do additions, substractions and multiplications. Make sure to greet the user.
#       1) Greet the user using INPUT and PRINT()
#       2) Addition: Ask for two numbers using INPUT and print the result of the addition
#       3) Substraction: Ask for two more numbers and print the result of the substraction
#       4) Multiplication: Ask for three more numbers and print the result of the multiplication
#       5) Thank them for using the your Calculator


###     HOMEWORK SOLUTION     ###

# Greet the user
name = input("What is your name?: ")
print(name)
print("Welcome "+ name + " to my calculator!")

# Addition of 2 numbers entered by the user
print("ADDITION")
x = input("First number: ")
y = input("Second number: ")
addition = int(x)+int(y)
print(addition)

# Subtraction of 2 numbers entered by the user
print("SUBTRACTION")
x = input("First number: ")
y = input("Second number: ")
subtraction = int(x)-int(y)
print(subtraction)

# Multiplication of 3 numbers entered by the user
print("MULTIPLICATION")
x = input("First number: ")
y = input("Second number: ")
z = input("Third number: ")
multiplication = int(x)*int(y)
print(multiplication)

# Thank you message
print("Thank you for using my Calculator!")

