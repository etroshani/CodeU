## Welcome to your 3rd CodeU Class! ##

####    FIRST PART    ####

# Recap of last classes material: 
#       -print()
#       -additions, substractions, and multiplications using Python
#       -Strings, Integers, Floats


###     HOMEWORK SOLUTION     ###

# Greet the user
name = "Johnny"
print("Welcome "+ name + " to my calculator!")

# Addition of 2 numbers: 123 456 and 876 544
x = 123456
y = 876544
addition = x + y
print(addition)

# Subtraction of 2 numbers: 10 000 and 555
x = 10000
y = 555
subtraction = x-y
print(subtraction)

# Multiplication of 3 numbers: 25, 26, and 27
x = 25
y = 26
z = 27
multiplication = x*y*z
print(multiplication)

# Thank you message
print("Thank you for using my Calculator!")




####    SECOND PART    ####

#   In the second part, we'll learn how to use INPUT. This will be the first interactive code the you will make!
#   You'll learn how to use INPUT with strings, integers and floats.


##  1. Strings, Integers, Floats and Booleans  ##

strings = "A string is a sequence of characters that is read as ONE element. It can be letters, numbers, symbols, and emojis"

integers = 5    # An Integer(int) is a value used to represent real numbers that DO NOT HAVE decimals("numbers after the comma").

floats = 5.55   # A Float(float) is a value used to represent real numbers that HAVE decimals("numbers after the comma").

Booleans = True    # Boolean statements are statements that evaluate to be true or false.
Booleans = False   


## 2. Introduction to INPUT! ##

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


###     CODE HERE     ###
