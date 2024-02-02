##  Welcome to your 4th CodeU Class!  ##


####    FIRST PART    ####

##   Recap of what was taught last class:   ## 
#       -Strings, Integers, Floats, and Booleans
#       -Input() Function

##   Homework Correction   ##

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




####    SECOND PART    ####


##   1) Continuation of INPUT    ##

# Example: What year are you born in?
name = input("What is your name: ")
age = input("How old are you?: ") 
dateofbirth = 2022 - int(age)
print(name + " is born in " + str(dateofbirth))


##     2) Introduction to CONDITIONALS     ##

# Example 1
animal = "cow"
if animal == "cow":
    print("MOO!!")
elif animal == "cat":
    print("Miaow!!")
elif animal == "dog":
    print("WOOF!")
else:
    print("That is not an animal!")




###     HOMEWORK   |    ONE Question Quiz ###

#   Homework Description   #
# You must create a ONE question Quiz where the user must answer correctly or else they lose the game! The question can be about
# any subject or topic you would like. You must let the user know if they answered correctly or incorrectly. 

#   STEPS   #
#   1) Create a variable unsing the input() function. This will log the user's answer to your question.
#   2) Create a condition IF where the user's answer must be equal to the correct answer.
#   2.1) Print a message letting the user know they answered correctly!
#   3) Create a condition ELSE that catches any other possible answer.
#   3.1) Print a message letting the user know they answered incorrectly!



###     CODE HERE     ###

